#!/usr/bin/env python3
"""Local smoke checker for contestant submissions.

This script validates the public interface contract only:
- submission contains solution.py with DocFusionSolution
- train() and predict() are callable
- predictions JSONL matches expected format and test IDs

It does NOT compute scores and does NOT mirror full judge benchmarking.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import traceback
import uuid
from pathlib import Path


def _load_solution(submission_dir: Path):
    solution_path = submission_dir / "solution.py"
    if not solution_path.exists():
        raise FileNotFoundError(f"No solution.py found in {submission_dir}")

    module_key = f"_submission_solution_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_key, solution_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load Python module from {solution_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_key] = module
    spec.loader.exec_module(module)

    if not hasattr(module, "DocFusionSolution"):
        raise AttributeError(
            f"solution.py in {submission_dir} must define a class named DocFusionSolution"
        )

    return module.DocFusionSolution()


def _load_jsonl(path: Path) -> list[dict]:
    records = []
    with path.open() as f:
        for idx, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {idx}: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"Each JSONL row must be an object in {path}, line {idx}")
            records.append(value)
    return records


def _validate_predictions(predictions_path: Path, test_path: Path) -> list[str]:
    errors: list[str] = []
    test_records = _load_jsonl(test_path)
    expected_ids = {record.get("id") for record in test_records}

    prediction_ids: set[str] = set()
    predictions = _load_jsonl(predictions_path)

    for idx, pred in enumerate(predictions, start=1):
        if "id" not in pred:
            errors.append(f"line {idx}: missing required field 'id'")
            continue

        if "is_forged" not in pred:
            errors.append(f"line {idx}: missing required field 'is_forged'")

        record_id = pred.get("id")
        if not isinstance(record_id, str) or not record_id.strip():
            errors.append(f"line {idx}: 'id' must be a non-empty string")
        else:
            if record_id in prediction_ids:
                errors.append(f"line {idx}: duplicate prediction id '{record_id}'")
            prediction_ids.add(record_id)

        is_forged = pred.get("is_forged")
        if type(is_forged) is not int or is_forged not in (0, 1):
            errors.append(f"line {idx}: 'is_forged' must be integer 0 or 1")

        for field in ("vendor", "date", "total"):
            value = pred.get(field)
            if field in pred and value is not None and not isinstance(value, str):
                errors.append(f"line {idx}: '{field}' must be string or null")

    missing_ids = sorted(expected_ids - prediction_ids)
    extra_ids = sorted(prediction_ids - expected_ids)

    if missing_ids:
        errors.append(f"missing predictions for {len(missing_ids)} test IDs")
    if extra_ids:
        errors.append(f"predictions contain {len(extra_ids)} unknown IDs")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a DocFusion contestant submission locally."
    )
    parser.add_argument(
        "--submission",
        required=True,
        help="Directory containing solution.py",
    )
    parser.add_argument(
        "--data",
        default="./dummy_data",
        help="Directory containing train/ and test/ (default: ./dummy_data)",
    )
    parser.add_argument(
        "--work-dir",
        default="./tmp_work",
        help="Directory where predictions will be written (default: ./tmp_work)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show traceback on failure",
    )
    args = parser.parse_args()

    submission_dir = Path(args.submission).resolve()
    data_dir = Path(args.data).resolve()
    work_dir = Path(args.work_dir).resolve()
    train_dir = data_dir / "train"
    test_dir = data_dir / "test"
    test_path = test_dir / "test.jsonl"

    for required_path in (submission_dir, train_dir, test_dir, test_path):
        if not required_path.exists():
            print(f"[check] ERROR: missing required path: {required_path}")
            return 1

    os.makedirs(work_dir, exist_ok=True)
    predictions_path = work_dir / "predictions.jsonl"

    try:
        solution = _load_solution(submission_dir)

        print(f"[check] Loaded submission: {submission_dir}")
        model_dir = solution.train(str(train_dir), str(work_dir))
        if not isinstance(model_dir, str) or not model_dir.strip():
            raise TypeError("train() must return a non-empty string path")

        solution.predict(model_dir, str(test_dir), str(predictions_path))

        if not predictions_path.exists():
            raise FileNotFoundError(
                f"predict() did not write predictions file: {predictions_path}"
            )

        errors = _validate_predictions(predictions_path, test_path)
        if errors:
            print("[check] FAILED")
            for error in errors:
                print(f"- {error}")
            return 1

        test_count = len(_load_jsonl(test_path))
        pred_count = len(_load_jsonl(predictions_path))
        print("[check] PASSED")
        print(f"[check] test records: {test_count}")
        print(f"[check] predictions:  {pred_count}")
        print(f"[check] output:       {predictions_path}")
        return 0

    except Exception as exc:
        print(f"[check] ERROR: {type(exc).__name__}: {exc}")
        if args.verbose:
            print(traceback.format_exc())
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

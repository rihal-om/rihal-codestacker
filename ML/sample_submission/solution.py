"""
Sample submission for the DocFusion competition.

Replace the train() and predict() methods with your own implementation.
You do NOT need to inherit from DocFusionSolution — as long as your class
is named DocFusionSolution and has these two methods, the harness will run it.
"""

import json
import os


class DocFusionSolution:
    def train(self, train_dir: str, work_dir: str) -> str:
        """
        Train your model here.

        For this baseline we do nothing and return a placeholder model directory.
        """
        model_dir = os.path.join(work_dir, "model")
        os.makedirs(model_dir, exist_ok=True)
        # TODO: train your model and save artifacts to model_dir
        return model_dir

    def predict(self, model_dir: str, data_dir: str, out_path: str) -> None:
        """
        Run inference and write predictions to out_path.

        For this baseline we predict null fields and genuine for every record.
        """
        test_jsonl = os.path.join(data_dir, "test.jsonl")
        with open(test_jsonl) as f:
            records = [json.loads(line) for line in f]

        with open(out_path, "w") as f:
            for r in records:
                prediction = {
                    "id": r["id"],
                    "vendor": None,   # TODO: predict vendor name
                    "date": None,     # TODO: predict date
                    "total": None,    # TODO: predict total amount
                    "is_forged": 0,   # TODO: predict 0 (genuine) or 1 (forged)
                }
                f.write(json.dumps(prediction) + "\n")
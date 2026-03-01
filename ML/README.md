# 2026 ML Rihal CodeStacker Challenge

## DocFusion: Operation Intelligent Documents

### **Storyline**

Across multiple government and enterprise departments, thousands of documents are processed every day—invoices, receipts, forms, and scanned reports. Most of this information is **locked inside unstructured PDFs and images**, requiring manual extraction, validation, and review. This slows down decision-making, introduces human error, and prevents organizations from reacting quickly to anomalies or suspicious activity.

To solve this, the **DocFusion Initiative** has been launched.
Your mission is to design an **intelligent, efficient, and production-ready document processing pipeline** that can:

1. **Understand** scanned documents.
2. **Extract** structured information.
3. **Detect** unusual or suspicious patterns automatically.

The goal is not only accuracy—but also **speed, reliability, and real-world deployability**.

### **Problem Statement**

You are provided with a unified scope of **scanned business documents** (a combination of SROIE, Find-It-Again, and CORD). Each document may contain:

* **Document identifiers** (invoice number, vendor name, date).
* **Monetary values** (totals, taxes, subtotals).
* **Layout variations and OCR noise**.

Your task is to transform these **unstructured documents** into:

1. **Clean structured data**.
2. **Anomaly detection insights**.
3. **A deployable ML pipeline suitable for automated evaluation**.

### **Your Challenge:**

You must design an end-to-end system that:

* Processes scanned PDFs/images.
* Extracts key structured fields accurately.
* Detects anomalous or suspicious records (using the Find-It-Again labels).
* Interfaces seamlessly with the **DocFusion Autograder Harness**.
* Operates efficiently under strict **time and resource constraints**.

### **The Data Foundation (Unified Corpus)**

To simulate a real-world environment with varying layouts, languages, and fraud scenarios, this challenge utilizes a **Unified Intersection** of three key datasets. Participants must treat these sources as a single, messy incoming stream of documents.

#### **Dataset A: SROIE (Scanned Receipts OCR and Information Extraction)**

* **Role:** The baseline for English receipt structure and OCR accuracy.
* **URL:** [SROIE Dataset on Kaggle](https://www.kaggle.com/datasets/urbikn/sroie-datasetv2)

#### **Dataset B: Find-It-Again (L3i)**

* **Role:** The "Red Team" dataset. It contains genuine SROIE receipts mixed with realistic forgeries (tampered text, copy-paste attacks). This is the ground truth for **Level 3 (Anomaly Detection)**.
* **URL:** [Find-It-Again Dataset (L3i Laboratory)](https://l3i-share.univ-lr.fr/2023Finditagain/index.html)

#### **Dataset C: CORD (Consolidated Receipt Dataset)**

* **Role:** The "Volume" dataset. Provides thousands of diverse layouts and noise variations to test the **robustness** of the pipeline.
* **URL:** [CORD Dataset on HuggingFace](https://huggingface.co/datasets/naver-clova-ix/cord-v2)

---

### **4. Objectives & Challenge Levels**

#### **Level 1: Document Understanding & EDA**

**Organizations cannot fix what they cannot see.**
Your first step is to explore and understand the unified dataset.

**Tasks:**

* Inspect document images and OCR outputs from all three sources.
* Clean and preprocess extracted text/data.
* Analyze common layouts, fields, and value distributions.
* Visualize dataset statistics (e.g., price distribution, vendor frequency) and potential anomalies.

**Goal:** Build intuition about the data and prepare it for modeling.

#### **Level 2: Structured Information Extraction**

**Manual data entry must be eliminated.**
Your task is to **automatically extract structured fields** from documents. Your pipeline must successfully extract the following mandatory fields:

* `vendor`: The merchant or company name.
* `date`: The transaction date.
* `total`: The total amount.

**Requirements:**

* Handle OCR noise and layout variations from the diverse CORD/SROIE samples.
* Format the final output to match the harness requirements (JSONL).

**Expected Outcome:** A reliable document-to-data extraction pipeline.

#### **Level 3: Anomaly Detection & Basic Web UI**

**Extracted data is only useful if it leads to actionable insight.**

**Part A: Detect Anomalies**
Identify suspicious or unusual documents. You must output an `is_forged` prediction (1 for forged, 0 for genuine). Training and extraction can use the unified corpus, while anomaly labels are anchored to the Find-It-Again mapping in the evaluation data. Look for:

* Abnormally high totals or statistical outliers.
* Missing or inconsistent fields (e.g., Total != Sum of parts).
* **Visual Forgery:** Evidence of copy-paste or digital tampering.

**Part B: Basic Web UI**
Develop a simple web-based dashboard (e.g., using Streamlit, Gradio, Django) to display your findings.

* **Input:** Allow users to upload a receipt image.
* **Output:** Display the image alongside the extracted fields and the anomaly status.
* **Visuals:** Highlight the "Suspicious" fields or bounding boxes directly on the document image.

**Goal:** Combine programmatic output for the autograder with a visual interface for human stakeholders.

#### **Level 4: Harness Integration & Pipeline Efficiency**

**The auditing process needs to be automated, seamless, and production-ready.**
Your pipeline will be rigorously tested by the **DocFusion Autograder Harness**, measuring speed, memory, and effectiveness.

**Part A: The Interface Contract**
You must implement a `solution.py` file containing the `DocFusionSolution` class at the project root. This class must handle both training and prediction:

```python
class DocFusionSolution:
    def train(self, train_dir: str, work_dir: str) -> str:
        """
        Train a model on data in train_dir.
      
        Args:
            train_dir: Path to directory containing train.jsonl and images/
            work_dir:  Scratch directory for writing model artifacts
          
        Returns:
            Path to the saved model directory (typically inside work_dir)
        """
        pass
  
    def predict(self, model_dir: str, data_dir: str, out_path: str) -> None:
        """
        Run inference and write predictions to out_path.
      
        Args:
            model_dir: Path returned by train()
            data_dir:  Path to directory containing test.jsonl and images/
            out_path:  Path where predictions JSONL should be written
        """
        pass
```

**Prediction output format (`predictions.jsonl`)**

Each line must be a JSON object, for example:

```json
{"id":"t001","vendor":"ACME Corp","date":"2024-01-01","total":"10.00","is_forged":0}
{"id":"t002","vendor":null,"date":null,"total":null,"is_forged":1}
```

Required fields:

* `id` (string, must match test ID)
* `is_forged` (integer, `0` or `1`)

Optional fields:

* `vendor` (string or `null`)
* `date` (string or `null`)
* `total` (string or `null`)

### **Local Validation Kit**

This repository includes a lightweight local validation kit for participants:

* `sample_submission/solution.py` - Starter template.
* `dummy_data/` - Small train/test dataset for local checks.
* `check_submission.py` - Smoke test for interface and output format.

`dummy_data/` is only for local smoke testing and schema validation. Final judge runs use private competition data.

Run local validation:

```bash
cd ML
python3 check_submission.py --submission ./sample_submission
```

If your submission is in another folder:

```bash
cd ML
python3 check_submission.py --submission /path/to/your/submission
```

The checker validates:

* `solution.py` defines `DocFusionSolution`.
* `train(train_dir, work_dir)` runs and returns a model directory path.
* `predict(model_dir, data_dir, out_path)` writes `predictions.jsonl`.
* Every prediction has required fields:
  * `id` (non-empty string)
  * `is_forged` (integer `0` or `1`)
* Optional fields `vendor`, `date`, `total` are string or `null`.
* Prediction IDs match the IDs in `dummy_data/test/test.jsonl` (no missing/duplicate/unknown IDs).

> Note: This checker does not calculate final scores and does not replace the private judge harness.

**Part B: Performance Optimization**
The harness will automatically benchmark your code. **Accuracy alone is not enough.** You must optimize:

* **Inference latency** and throughput per document.
* **Peak memory usage** during both training and prediction.
* **Model size** (disk and memory footprint).

**Part C: Reproducibility & ML Engineering**
Show production discipline by including:

* Clear project structure.
* Strict dependency management (e.g., `uv`, `poetry`, `requirements.txt`, etc.).
* Deterministic execution to ensure your code runs seamlessly in the judge's environment.

**Goal:** Deliver a robust system that passes automated testing and could realistically run inside an enterprise workflow.

---

### **5. Bonus Task: Intelligent Automation & Deployment**

**Can your system operate in the real world?**
These are **optional extensions** but will strengthen your submission.

* **Containerization:** Create a **Dockerfile** to containerize your project (Model + UI). Ensure all OCR dependencies and libraries are included. Efficient image/build design is a plus.
* **Cloud Deployment:** Deploy your application on a VPS or cloud platform. Provide a public demo link and/or deployed endpoint.
* **Intelligent Assistance:** Use a lightweight LLM to generate **human-readable anomaly summaries** (e.g., *"This receipt appears tampered; the date font does not match the vendor font"*).

---

### **6. Submission Guidelines**

#### **What to Submit:**

1. **Full Source Code**: The entire codebase, including training scripts, inference code, and UI components.
2. **`solution.py`**: The file must exist in the root and it must contain the `DocFusionSolution` class exactly as specified in the interface contract.
3. **Dependencies**: A clear `pyproject.toml` or `requirements.txt` and lockfile. Python 3.13+ is required.
4. **Jupyter Notebooks**: Documenting your Level 1 EDA, model training logic, and extraction experiments.
5. **Web UI Code**: Scripts to run your Level 3 dashboard (e.g., `app.py`).
6. **Documentation**: A comprehensive README explaining your approach, architecture, and instructions for running your UI and Docker containers.

**Final Note:**
Creativity, clarity, and real-world thinking are strongly encouraged. The strongest solutions will demonstrate **production awareness, efficiency, and thoughtful engineering design**.

We look forward to seeing how you transform raw documents into intelligent decisions.

## **Happy coding - and welcome to CodeStacker 2026.**

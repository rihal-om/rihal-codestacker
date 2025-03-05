# 2025 ML Rihal Codestacker Challenge

## CityX Crime Watch: Operation Safe Streets

### **Storyline**

CityX, once a peaceful metropolis, is facing an alarming surge in criminal activity. The local police department has been diligently collecting historical and real-time incident reports, but the volume of data is overwhelming. They need your help to find hidden patterns, predict future hotspots, and build an efficient system to respond to crime faster and keep citizens safe.

Your mission? Use the CityX crime dataset and apply ML-based approaches to explore and analyze patterns. The end goal is to help the police with data-driven insights to intervene whenever necessary.

## **Problem Statement**

The CityX Police Department has aggregated a comprehensive crime dataset spanning several years. Each record in the dataset includes:

* **Dates**: Timestamp of the crime incident
* **Category**: Category of the crime incident
* **Descript**: Detailed description of the crime incident
* **DayOfWeek**: The day of the week
* **PdDistrict**: Name of the Police Department District
* **Resolution**: How the crime incident was resolved
* **Address**: The approximate street address of the crime incident
* **Longitude (X)**: Longitude
* **Latitude (Y)**: Latitude

## **Your Challenge**

* Clean and preprocess the data
* Uncover patterns and trends
* Classify crimes into categories
* Generate descriptive narratives for incidents
* Visualize crime patterns with geo-spatial mapping and clustering analyses
* Forecast future crime frequencies and hotspots

## **Objectives & Challenge Levels**

### **Level 1: Exploratory Data Analysis (EDA)**

**Crime data is piling up, and the police need your help to make sense of it!**

* Familiarize yourself with the dataset and extract key insights.
* Clean and preprocess the raw data.
* Summarize important features.
* Visualize trends.

### **Level 2: Crime Classification & Severity Assignment**

**The police need your help with categorizing crimes quickly!**

#### **Part A: Predicting Crime Type**

* Build a model to classify crimes based on their description (`Descript`).
* The goal is to predict the crime category (`Category`) using supervised learning.
* Evaluate the model’s accuracy and discuss potential improvements.

#### **Part B: Assigning Crime Severity**

* Classify each crime into the following severity levels based on its category:
    * **Severity 1**: NON-CRIMINAL, SUSPICIOUS OCCURRENCE, MISSING PERSON, RUNAWAY, RECOVERED VEHICLE
    * **Severity 2**: WARRANTS, OTHER OFFENSES, VANDALISM, TRESPASS, DISORDERLY CONDUCT, BAD CHECKS
    * **Severity 3**: LARCENY/THEFT, VEHICLE THEFT, FORGERY/COUNTERFEITING, DRUG/NARCOTIC, STOLEN PROPERTY, FRAUD, BRIBERY, EMBEZZLEMENT
    * **Severity 4**: ROBBERY, WEAPON LAWS, BURGLARY, EXTORTION
    * **Severity 5**: KIDNAPPING, ARSON
* This part can be implemented using simple conditional logic.
* Output both **predicted crime type** and **assigned severity**.

### **Level 3: Geo-Spatial Mapping & Basic Web UI**

**CityX needs an interactive crime map to visualize crime trends!**

#### **Part A: Geo-Spatial Visualization**

* Build interactive crime maps (e.g., using Folium, Plotly, or GeoPandas).
* Feel free to explore different ways to visualize the dataset and create dynamic, engaging maps.

#### **Part B: Basic Web UI**

* Develop a simple web-based dashboard (e.g., using Streamlit, Flask, Dash etc..) to display your findings.
* Integrate your geo-spatial map into the dashboard to let users explore crime hotspots interactively.

### **Level 4: Advanced Web UI & Report Extraction**

**Officers receive reports in PDF format. Can you extract and process them automatically?**

#### **Part A: Police Report Extraction**

* You’ll be provided with sample police reports in PDF format.
* Your task is to automatically extract key fields aligned with the task at hand.

#### **Part B: Integration with Classifier**

* Convert this data into a structured format and feed it into your model from Level 2.
* Predict the crime category and severity.

#### **Part C: Enhanced Web UI**

* Design a web interface that automatically populates a **table** (serving as a "form") with the extracted data.
* This table should mirror the input fields of the dataset used to train your model.
* The data in this table should be used as input to perform inference on your trained model.
* Ensure your Web UI integrates with all the challenges from the previous levels.

## **Bonus Task: Deployment**

**Can you take your project to production?**

This is an **optional challenge** that allows you to showcase your ability to deploy and scale a real-world ML application. Completing this task will increase your chances of winning the competition.

### **Part A: Dockerization & Containerization**

* Create a **Dockerfile** to containerize your project, ensuring all dependencies are included.
* The container should encapsulate **data preprocessing, model inference, and the web dashboard** in a reproducible environment.

### **Part B: Cloud Deployment**

* Deploy your application on a **Virtual Private Server (VPS)** or cloud platform such as:
* **Cloudflare, DigitalOcean, Heroku, Vercel, AWS, GCP, or Azure**.
* Ensure the web UI and model inference pipeline are accessible from a **public URL**.

## **Submission Guidelines**

* **Levels 1 & 2 (Data Analysis & Modeling):**
    * Submit your work as a **Jupyter Notebook (.ipynb)** including all exploratory data analysis, preprocessing steps, model training, evaluation, and any visualizations.
    * Ensure your notebook is well-commented and contains narrative explanations.
* **Levels 3 & 4 (Web UI & Report Extraction):**
    * Submit your project as **code files**, including scripts (e.g., `app.py` for a Streamlit dashboard or equivalent) along with necessary support files (e.g., `requirements.txt`).
    * Include a **README** with clear instructions on how to run your application, dependencies, and additional notes.
* **Bonus Task:**
    * Provide a **link to your deployed application**.
    * Submit your **Dockerfile**, deployment scripts, and a **README** explaining how to run and deploy the project.
    * Optionally, include a **short video demo** showcasing your deployed application.

## **Note**

Bonus grades will be awarded to those who demonstrate **creativity and innovation** beyond the core requirements. We encourage you to add extra features, write **clean and well-documented** code, and follow **best practices** in development and deployment. Extra credit will be awarded for **scalable, production-ready solutions** that showcase your unique approach to the challenge.

### \*\*Happy coding! \*\*
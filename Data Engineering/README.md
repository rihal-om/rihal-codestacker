# 🚨 Data Egineering Pipline Challenge

## 📚 Background

CityX is a busy, crowded city that is currently experiencing a surge in crime incidents across its multiple districts. City officials are struggling to manage crime effectively due to inaccurate records and poorly maintained district information. The districts each have unique attributes such as population and governance, but this data has spelling mistakes and inaccuracies. Authorities urgently require clean, reliable data to track and manage crime efficiently.

## 📝 Problem Statement

You are required to develop a data engineering solution to integrate and clean data from two distinct sources:
- **Crime event records** provided in a JSON file (`crimes_data.json`) 📄.
- **District details** extracted from a scanned PDF document (`districts_info.pdf`) 📑.

This system will process, transform, and merge data from these two sources to provide clean, actionable information to city officials.

## 🎯 Objectives

- Extract and clean data from the provided JSON (crime data) and PDF (district info) using Python. 🐍
- Perform the required transformations and cleansing as detailed in the steps below.
- Merge the datasets and load the cleaned, transformed data into a database.
- *(Optional)* Create a web app or dashboard visualizing key crime metrics. 📊

## 🔍 Steps

1. **Data Ingestion and OCR**  
   - **Crime Records:**  
     - Use Pandas, Polars, or any other Python library to load crime event records from the provided JSON file. The records include:
       - `district_id`, `timestamp`, `crime_type`, and `nearest_police_patrol`.  
   - **District Information:**  
     - Extract district information from the provided scanned PDF file using OCR libraries in Python.  
     - The extracted district info table has the following columns:
       - `district_id`, `location`, `population`, `Governor`.

2. **Data Cleaning and Transformation**  
   - **Crime Records Table:**  
     - Remove invalid records (i.e., records with missing `crime_type`). ❌  
     - Correct any spelling mistakes in the `crime_type` values. 🔠  
     - Standardize distances in `nearest_police_patrol` (convert all to kilometers; original values may be in miles or kilometers). 📏  
     - Split the `timestamp` into three new columns: `day_of_week`, `date`, and `time`. ⏰  
   - **District Information Table:**  
     - Programmatically correct spelling mistakes in the `location` field. 📝  
     - Rename the `location` column to `district_name`. ✏️

3. **Data Integration**  
   - Merge the crime records table with the district information table on the `district_id` field. 🔗  
   - The final table should include the following fields:

     | district_id | district_name | crime_type | nearest_police_patrol | population | governor | day_of_week | date       | time     |
     |-------------|---------------|------------|-----------------------|------------|----------|-------------|------------|----------|
     | ...         | ...           | ...        | ...                   | ...        | ...      | ...         | ...        | ...      |

4. **Data Storage**  
   - Insert the processed, clean data into a database of your choice that is deployed using Docker (e.g., PostgreSQL, MySQL). 🐳

5. **Optional Visualization (Bonus Points)**  
   - Create a simple dashboard or web app using Streamlit (or any similar visualization tool) to answer the following:
     - Which district has the highest crime rate? 📈  
     - Which day of the week has the highest number of crimes? 📅  
     - Which district has the highest average distance between crime locations and the nearest police patrol? 📊

## 🐳 Containerization

All pipeline components must be containerized using Docker. (The optional dashboard component may be run separately.)

## 📤 Submission Guidelines

**Required:**
- Create a GitHub repository including:
  - Source code.
  - Dockerfiles for all components and a Docker Compose file for easy setup.
  - A clear README with instructions for setup, running, and testing your project.

**Optional:**
- Provide a simple dashboard visualizing key insights (e.g., using Streamlit).
- Optionally, submit a brief demo video showcasing your solution's capabilities.

Submit your repository link and demo video (if applicable) to the email (info@rihal.om) as per the provided submission instructions.

---

Good luck, and happy coding! 🚀

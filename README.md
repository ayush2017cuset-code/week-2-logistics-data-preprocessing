# Week 2 – Logistics Data Collection, Cleaning and Preprocessing

## Project Overview

This project demonstrates a data collection, cleaning, and preprocessing pipeline for logistics analysis using Python. The objective is to prepare supply-chain data for further analysis by identifying and addressing common data-quality issues.

## Objectives

* Load and inspect a logistics dataset
* Identify missing values
* Handle missing values
* Remove duplicate records
* Correct data types
* Calculate delivery delay
* Detect outliers using the IQR method
* Standardize categorical text
* Normalize numerical variables
* Prepare data for further analysis

## Dataset

The project uses the **DataCo Supply Chain Dataset**, a publicly available logistics and supply-chain dataset obtained from Kaggle.

The dataset contains information related to customers, orders, sales, shipping, delivery status, product categories, shipping duration, and other supply-chain variables.

The original dataset is not included in this repository because of its large file size.

## Technologies Used

* Python
* Pandas
* Scikit-learn

## Preprocessing Steps

### 1. Loading and Initial Inspection

The dataset is loaded using Pandas. Initial inspection is performed to understand the dataset dimensions, data types, and missing values.

### 2. Handling Missing Values

Missing customer ZIP codes are replaced with `Unknown`.

Missing values in the `Order Item Discount` column are handled using median imputation.

### 3. Removing Duplicates

Duplicate rows are identified and removed to improve data consistency.

### 4. Correcting Data Types

Order and shipping date columns are converted into datetime format. A delivery-delay variable is calculated from the difference between shipping and order dates.

### 5. Outlier Detection

The Interquartile Range (IQR) method is used to identify potential outliers in the `Benefit per order` variable.

### 6. Standardizing Categorical Text

Categorical variables such as `Category Name` and `Customer Segment` are cleaned by removing unnecessary spaces and standardizing capitalization.

### 7. Normalization

Min-Max scaling is applied to numerical variables such as sales and shipping duration so that they are transformed to a common scale.

## Project Files

* `README.md` – Project documentation
* `logistics_preprocessing.py` – Python preprocessing script
* `Week_2_Logistics_Report.docx` – Detailed internship report

## Python Implementation

The preprocessing operations are implemented using Pandas and Scikit-learn. The Python script follows the methodology described in the submitted report.

## Conclusion

Data cleaning and preprocessing are important steps in logistics analytics because inaccurate, incomplete, duplicated, or inconsistent data can affect analytical results and decision-making. This project demonstrates a systematic approach to preparing logistics data for subsequent analysis.

## Dataset Source

The dataset used in this project was obtained from Kaggle.

Source:
www.kaggle.com/code/nilufarhosseini/supply-chain-data-analysis-99-accuracy/input


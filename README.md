# 📊 Task 02 – Split Data for Training and Testing

> **Machine Learning Internship Project – Saiket Systems**

## 📌 Overview

This project is the second task of my **Machine Learning Internship at Saiket Systems**. The primary objective of this task is to divide a preprocessed dataset into **training** and **testing** subsets, which is a fundamental step in the machine learning workflow.

A proper train-test split ensures that a machine learning model learns from one portion of the data and is evaluated on completely unseen data, allowing us to measure its real-world performance.

---

# 🎯 Objectives

* Load the cleaned Telco Customer Churn dataset.
* Separate the dataset into **features (X)** and **target variable (y)**.
* Split the dataset into **80% training** and **20% testing** sets.
* Preserve the class distribution using stratified sampling.
* Save the generated datasets for future model training and evaluation.

---

# 📂 Dataset Information

**Dataset Name:** Telco Customer Churn Dataset

The dataset contains customer information from a telecommunications company, including demographic details, subscribed services, billing information, and customer churn status.

### Target Variable

**Churn**

* **1** → Customer has churned.
* **0** → Customer has not churned.

---

# 🛠️ Technologies Used

* Python 3
* Pandas
* NumPy
* Scikit-learn

---

# 📚 Libraries

```python
import pandas as pd
from sklearn.model_selection import train_test_split
```

---

# ⚙️ Project Workflow

## Step 1 – Load the Dataset

The cleaned dataset generated during Task 01 is loaded using the Pandas library.

---

## Step 2 – Explore the Dataset

Basic dataset information is displayed, including:

* Number of rows
* Number of columns
* Dataset preview
* Feature count

---

## Step 3 – Separate Features and Target

The dataset is divided into:

### Features (X)

Independent variables used by the model for prediction.

Examples:

* Gender
* Partner
* Tenure
* MonthlyCharges
* InternetService
* Contract

### Target (y)

The dependent variable:

**Churn**

This is the value that the machine learning model will predict.

---

## Step 4 – Train-Test Split

The dataset is divided using Scikit-learn's `train_test_split()` function.

```python
train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
```

### Parameters

### `test_size = 0.20`

* 80% → Training Dataset
* 20% → Testing Dataset

### `random_state = 42`

Ensures reproducible results by generating the same split every time the program is executed.

### `stratify = y`

Maintains the same class distribution in both training and testing datasets, preventing class imbalance.

---

# 📊 Output

After executing the program, the dataset is divided into:

| Dataset          | Records |
| ---------------- | ------: |
| Training Dataset |    5634 |
| Testing Dataset  |    1409 |

Generated files:

* X_train.csv
* X_test.csv
* y_train.csv
* y_test.csv

---

# 📁 Project Structure

```text
Task-02/
│
├── task-02.py
├── README.md
├── Clean_Telco_Customer_Churn.csv
├── X_train.csv
├── X_test.csv
├── y_train.csv
└── y_test.csv
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Move into the project folder:

```bash
cd Task-02
```

Install the required dependencies:

```bash
pip install pandas numpy scikit-learn
```

---

# ▶️ Run the Project

```bash
python task-02.py
```

---

# ✅ Expected Output

```
Dataset loaded successfully!

Training Features : (5634, 19)
Testing Features  : (1409, 19)

Training Labels   : (5634,)
Testing Labels    : (1409,)

Training Data Percentage : 80%
Testing Data Percentage  : 20%

Task Completed Successfully
```

---

# 💡 Key Concepts Learned

* Machine Learning Data Pipeline
* Feature and Target Separation
* Train-Test Splitting
* Stratified Sampling
* Data Preparation
* Reproducible Experiments
* Scikit-learn Workflow

---

# 🚀 Skills Demonstrated

* Python Programming
* Data Analysis
* Data Preparation
* Pandas
* NumPy
* Scikit-learn
* Machine Learning Fundamentals
* Train-Test Split
* Data Handling

---

# 📖 Learning Outcome

By completing this project, I gained practical experience in preparing datasets for machine learning by implementing a standard train-test split strategy. I also learned the importance of maintaining class balance using stratified sampling and ensuring reproducibility using a fixed random state. These are essential practices for building reliable and unbiased machine learning models.

---

# 🙏 Acknowledgement

This project was completed as **Task 02** during my **Machine Learning Internship at Saiket Systems**. It provided valuable hands-on experience in one of the core stages of the machine learning pipeline and strengthened my understanding of data preparation for model development.

---

## ⭐ If you found this project useful, consider giving this repository a **Star** and feel free to explore my other machine learning internship projects.

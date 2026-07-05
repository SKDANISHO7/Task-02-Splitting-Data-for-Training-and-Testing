# 📊 Task 02 – Split Data for Training and Testing

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</p>

---

# 📌 Machine Learning Internship Project

**Organization:** Saiket Systems

**Role:** Machine Learning Intern

**Task:** Task 02 – Split Data for Training and Testing

---

# 📖 Project Overview

This project is the **second task** of my Machine Learning Internship at **Saiket Systems**.

The objective of this project is to prepare a machine learning dataset by dividing it into **Training** and **Testing** subsets using Scikit-learn's **train_test_split()** function.

A proper train-test split is one of the most important stages in the Machine Learning pipeline because it enables models to learn from one portion of the data while evaluating their performance on completely unseen data.

This approach helps build reliable, unbiased, and generalizable Machine Learning models.

---

# 🎯 Objectives

✔ Load the cleaned Telco Customer Churn dataset

✔ Separate Features (X) and Target (y)

✔ Perform an 80:20 Train-Test Split

✔ Maintain class balance using Stratified Sampling

✔ Ensure reproducible results using Random State

✔ Save all generated datasets

---

# 🖼 Project Workflow

> Add your generated workflow image here.

```md
![Workflow](images/workflow.png)
```

---

# 📸 Project Screenshots

## 💻 Python Implementation

```md
![Code](images/code.png)
```

---

## 🖥 Program Output

```md
![Output](images/output.png)
```

---

# 📂 Dataset Information

**Dataset Name**

Telco Customer Churn Dataset

The dataset contains customer information including

- Demographics
- Services subscribed
- Contract Information
- Payment Details
- Monthly Charges
- Customer Churn Status

### Target Variable

| Value | Meaning |
|--------|----------|
| 1 | Customer Churned |
| 0 | Customer Stayed |

---

# ⚙ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

---

# 📚 Libraries

```python
import pandas as pd
from sklearn.model_selection import train_test_split
```

---

# 🔄 Machine Learning Pipeline

```text
Load Dataset
      │
      ▼
Separate Features (X)
      │
      ▼
Separate Target (y)
      │
      ▼
Train-Test Split
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Train     Test
80%       20%
      │
      ▼
Ready for Model Training
```

---

# ⚙️ Project Workflow

## Step 1 — Load Dataset

The cleaned dataset generated in **Task 01** is loaded using Pandas.

---

## Step 2 — Explore Dataset

Dataset inspection includes:

- Shape
- Number of Columns
- Number of Rows
- Preview
- Data Types

---

## Step 3 — Feature & Target Separation

### Features (X)

All independent variables used for prediction.

Example

- Gender
- Partner
- Dependents
- Tenure
- Internet Service
- Contract

### Target (y)

Customer Churn

---

## Step 4 — Train-Test Split

```python
train_test_split(
X,
y,
test_size=0.20,
random_state=42,
stratify=y
)
```

---

# 📌 Parameter Explanation

## test_size = 0.20

20% data is reserved for testing.

Remaining 80% is used for training.

---

## random_state = 42

Ensures reproducible dataset splitting.

Every execution generates the same split.

---

## stratify = y

Maintains equal class distribution in

Training Dataset

and

Testing Dataset

---

# 📊 Output

| Dataset | Shape |
|---------|--------|
| X_train | (5634,19) |
| X_test | (1409,19) |
| y_train | (5634,) |
| y_test | (1409,) |

Generated Files

```
X_train.csv
X_test.csv
y_train.csv
y_test.csv
```

---

# 📁 Project Structure

```
Task-02/
│
├── images/
│   ├── workflow.png
│   ├── code.png
│   └── output.png
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

# ▶ Installation

```bash
git clone https://github.com/yourusername/Task-02.git

cd Task-02

pip install pandas numpy scikit-learn
```

---

# ▶ Run

```bash
python task-02.py
```

---

# ✅ Expected Output

```
Dataset loaded successfully!

Training Features : (5634, 19)

Testing Features : (1409, 19)

Training Labels : (5634,)

Testing Labels : (1409,)

Training Data : 80%

Testing Data : 20%

Task Completed Successfully
```

---

# 💡 Why Train-Test Split?

A Machine Learning model should never be evaluated using the same data on which it was trained.

Splitting the dataset allows us to

- Evaluate model performance fairly

- Reduce Overfitting

- Improve Generalization

- Build Reliable Models

---

# 🚀 Skills Demonstrated

- Python Programming

- Data Analysis

- Data Preparation

- Pandas

- NumPy

- Scikit-learn

- Feature Engineering

- Train-Test Splitting

- Stratified Sampling

- Machine Learning Workflow

---

# 📚 Learning Outcomes

After completing this project, I learned

- How Machine Learning datasets are divided

- Importance of Training and Testing datasets

- Feature & Target separation

- Reproducibility using random_state

- Balanced data splitting using stratify

- Preparing datasets for Machine Learning models

---

# 🚀 Future Scope

The generated datasets will be used in upcoming tasks to

- Train Machine Learning Models

- Evaluate Performance

- Compare Algorithms

- Predict Customer Churn

---

# 🙏 Acknowledgement

This project was completed as **Task 02** during my **Machine Learning Internship at Saiket Systems**.

It enhanced my understanding of data preparation and the importance of proper dataset splitting before model development.

---

# 👨‍💻 Author

**Shaikh Danish**

Machine Learning Intern — Saiket Systems

GitHub: https://github.com/YourUsername

LinkedIn: https://linkedin.com/in/YourProfile

---

⭐ **If you found this project helpful, don't forget to Star this repository!**

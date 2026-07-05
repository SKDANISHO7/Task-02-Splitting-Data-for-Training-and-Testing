# ============================================
# Task 02: Split Data for Training and Testing
# Machine Learning Internship - Saiket Systems
# ============================================

# Import Required Libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# ============================================
# Step 1: Load the Clean Dataset
# ============================================

try:
    df = pd.read_csv("Clean_Telco_Customer_Churn.csv")
    print(" Dataset loaded successfully!\n")
except FileNotFoundError:
    print(" Error: Clean dataset file not found.")
    print("Please complete Task 01 before running this program.")
    exit()

# ============================================
# Step 2: Display Dataset Information
# ============================================

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print(f"Number of Rows    : {df.shape[0]}")
print(f"Number of Columns : {df.shape[1]}")

print("\nFirst Five Rows:")
print(df.head())

# ============================================
# Step 3: Separate Features and Target Variable
# ============================================

# Features (Independent Variables)
X = df.drop("Churn", axis=1)

# Target (Dependent Variable)
y = df["Churn"]

print("\nFeature Matrix Shape :", X.shape)
print("Target Vector Shape  :", y.shape)

# ============================================
# Step 4: Split Dataset
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ============================================
# Step 5: Display Split Information
# ============================================

print("\n" + "=" * 50)
print("TRAINING AND TESTING DATA")
print("=" * 50)

print(f"Training Features : {X_train.shape}")
print(f"Testing Features  : {X_test.shape}")

print(f"Training Labels   : {y_train.shape}")
print(f"Testing Labels    : {y_test.shape}")

print("\nTraining Data Percentage : {:.0f}%".format(
    len(X_train) / len(df) * 100))

print("Testing Data Percentage  : {:.0f}%".format(
    len(X_test) / len(df) * 100))

# ============================================
# Step 6: Save Split Datasets
# ============================================

X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)

y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("\n Split datasets saved successfully!")

# ============================================
# Step 7: Display Target Distribution
# ============================================

print("\n" + "=" * 50)
print("TARGET VARIABLE DISTRIBUTION")
print("=" * 50)

print("\nTraining Dataset:")
print(y_train.value_counts())

print("\nTesting Dataset:")
print(y_test.value_counts())

# ============================================
# Task Completed
# ============================================

print("\n" + "=" * 50)
print("TASK 02 COMPLETED SUCCESSFULLY")
print("=" * 50)

print("""
Generated Files:
---------------
1. X_train.csv
2. X_test.csv
3. y_train.csv
4. y_test.csv

The dataset has been successfully divided into:
• 80% Training Data
• 20% Testing Data

The data is now ready for Machine Learning model training.
""")
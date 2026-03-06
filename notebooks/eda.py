import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Aashi/OneDrive/Documents/Ghost of Tsushima DIRECTOR'S CUT/exam_anxiety_dataset_clean.csv")

# Show first rows
print("First 5 rows of dataset:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Rename columns
df.rename(columns={
    "text": "statement",
    "anxiety_level": "status"
}, inplace=True)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove rows with missing statements
df = df.dropna(subset=['statement'])

# Verify again
print("\nMissing values after cleaning:")
print(df.isnull().sum())
//3.2.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:/Users/Aashi/OneDrive/Documents/Ghost of Tsushima DIRECTOR'S CUT/exam_anxiety_dataset_clean.csv")

# Show first rows
print(df.head())

# Plot distribution of labels
plt.figure(figsize=(8,5))

sns.countplot(x='anxiety_level', data=df)

plt.title("Original Label Distribution")
plt.xlabel("Mental Health Labels")
plt.ylabel("Count")

plt.show()
//3.3.py

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Aashi\OneDrive\Documents\Ghost of Tsushima DIRECTOR'S CUT\exam_anxiety_dataset_clean.csv")

# Show first rows
print(df.head())

# Show column names
print(df.columns)

# Remove missing values
df = df.dropna(subset=['text'])

# Label Mapping according to Activity 3.3
label_mapping = {
    "Normal": "Low Anxiety",
    "Stress": "Moderate Anxiety",
    "Anxiety": "Moderate Anxiety",
    "Depression": "High Anxiety",
    "Suicidal": "High Anxiety",
    "Bipolar": "High Anxiety",
    "Personality Disorder": "High Anxiety"
}

# Apply mapping
df["mapped_anxiety_level"] = df["anxiety_level"].map(label_mapping)

# Show result
print("\nMapped Dataset:")
print(df.head())
//3.4
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Aashi\OneDrive\Documents\Ghost of Tsushima DIRECTOR'S CUT\exam_anxiety_dataset_clean.csv")

# Check dataset
print(df.head())

# Mapping text labels to numbers
label_mapping = {
    'Low': 0,
    'Moderate': 1,
    'High': 2
}

# Create numerical label column
df['anxiety_label'] = df['anxiety_level'].map(label_mapping)

# Show result
print("\nDataset with numerical labels:")
print(df.head())

# Save new dataset
df.to_csv("exam_anxiety_dataset_numerical.csv", index=False)

print("Numerical labels created successfully!")

# Validate dataset
print("Missing values in anxiety_level column:")
print(df['anxiety_label'].isnull().sum())

print("\nDistribution of anxiety levels:")
print(df['anxiety_label'].value_counts())

# Plot graph (Fig 3.5)
df['anxiety_label'].value_counts().plot(kind='bar')

plt.title("Final Anxiety Level Distribution")
plt.xlabel("Anxiety Level (0=Low, 1=Moderate, 2=High)")
plt.ylabel("Count")

plt.show()







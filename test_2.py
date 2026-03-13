import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("data.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())

# -----------------------------
# 2. Create KPI Metrics
# -----------------------------

# Average score KPI
df["average_score"] = df[["math score","reading score","writing score"]].mean(axis=1)

# Pass/Fail KPI (50 threshold)
df["pass"] = df["average_score"] >= 50

# -----------------------------
# 3. Overall KPIs
# -----------------------------

print("\n===== OVERALL KPIs =====")

overall_avg = df["average_score"].mean()
pass_rate = df["pass"].mean() * 100

print(f"Overall Average Score: {overall_avg:.2f}")
print(f"Overall Pass Rate: {pass_rate:.2f}%")

# -----------------------------
# 4. KPI by Gender
# -----------------------------

print("\n===== PERFORMANCE BY GENDER =====")

gender_kpi = df.groupby("gender")[["math score","reading score","writing score","average_score"]].mean()

print(gender_kpi)

# -----------------------------
# 5. KPI by Test Preparation
# -----------------------------

print("\n===== TEST PREPARATION IMPACT =====")

prep_kpi = df.groupby("test preparation course")[["math score","reading score","writing score","average_score"]].mean()

print(prep_kpi)

# -----------------------------
# 6. KPI by Parental Education
# -----------------------------

print("\n===== PARENTAL EDUCATION IMPACT =====")

education_kpi = df.groupby("parental level of education")[["average_score"]].mean()

print(education_kpi)

# -----------------------------
# 7. Correlation Analysis
# -----------------------------

print("\n===== SCORE CORRELATIONS =====")

corr = df[["math score","reading score","writing score"]].corr()
print(corr)

# -----------------------------
# 8. Visualizations
# -----------------------------

sns.set(style="whitegrid")

# Score distributions
plt.figure(figsize=(8,5))
sns.histplot(df["average_score"], bins=20, kde=True)
plt.title("Distribution of Average Scores")
plt.show()


# Average score by gender
plt.figure(figsize=(6,4))
sns.barplot(x="gender", y="average_score", data=df)
plt.title("Average Score by Gender")
plt.show()


# Test preparation effect
plt.figure(figsize=(6,4))
sns.barplot(x="test preparation course", y="average_score", data=df)
plt.title("Impact of Test Preparation on Scores")
plt.show()


# Parental education impact
plt.figure(figsize=(8,5))
sns.barplot(
    x="parental level of education",
    y="average_score",
    data=df
)

plt.xticks(rotation=45)
plt.title("Average Score by Parental Education")
plt.show()


# Correlation heatmap
plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Score Correlation Matrix")
plt.show()

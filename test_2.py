import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('data.csv')

categorical_cols = [
    'gender',
    'race/ethnicity',
    'parental level of education',
    'lunch',
    'test preparation course'
]

numeric_cols = ['math score', 'reading score', 'writing score']

# Total number of plots
total_plots = len(categorical_cols) + len(numeric_cols)

# Set up subplots: 2 rows, 4 columns (adjust as needed)
fig, axes = plt.subplots(2, 4, figsize=(12, 6))  # Smaller figure size

# Flatten axes for easy iteration
axes = axes.flatten()

# Plot categorical columns
for i, col in enumerate(categorical_cols):
    df[col].value_counts().plot(kind='bar', ax=axes[i])
    axes[i].set_xlabel('')
    axes[i].set_ylabel('Count')
    axes[i].set_title(col)

# Plot numeric columns
for j, col in enumerate(numeric_cols):
    df[col].plot(kind='hist', bins=20, edgecolor='black', ax=axes[len(categorical_cols) + j])
    axes[len(categorical_cols) + j].set_ylabel('Frequency')
    axes[len(categorical_cols) + j].set_title(col)

# Hide any unused subplots
for k in range(total_plots, len(axes)):
    fig.delaxes(axes[k])

plt.tight_layout()
plt.show()

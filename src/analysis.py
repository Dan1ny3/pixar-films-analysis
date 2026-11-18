import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Asigura existenta folderului pentru grafice
os.makedirs("images", exist_ok=True)

# Incarcare date folosind cale relativa
file_path = os.path.join("data", "pixar_films.xlsx")
df = pd.read_excel(file_path)

selected_columns = [
    "box_office_worldwide",
    "rotten_tomatoes_score",
    "metacritic_score",
    "imdb_score",
]

clean_df = df[selected_columns].dropna()
matrix = clean_df.to_numpy()
np.set_printoptions(suppress=True)

# Statistici descriptive
average = np.mean(matrix, axis=0)
median = np.median(matrix, axis=0)
mode = stats.mode(matrix, axis=0, keepdims=False)[0]
range_values = np.ptp(matrix, axis=0)
std_dev = np.std(matrix, axis=0)

print("=== Descriptive Statistics ===")
for i, col in enumerate(selected_columns):
    print(f"\nColumn: {col}")
    print(f"  Mean: {average[i]:.2f}")
    print(f"  Median: {median[i]:.2f}")
    print(f"  Mode: {mode[i]:.2f}")
    print(f"  Range: {range_values[i]:.2f}")
    print(f"  Std Dev: {std_dev[i]:.2f}")

# Matricea de corelatie (salvata si ca imagine pentru README)
plt.figure(figsize=(8, 6))
correlation_matrix = clean_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix - Pixar Films Metrics")
plt.tight_layout()
plt.savefig("images/correlation_matrix.png", dpi=300)
plt.show()
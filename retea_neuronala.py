# Importuri necesare
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
from scipy import stats
from IPython.display import display

# Montam Google Drive
drive.mount('/content/drive')

# Calea fisierului
file_path = "/content/drive/My Drive/pixar_films new.csv"
df = pd.read_excel(file_path)

# Afisarea matricei din fisierul .csv
display(df)

# Afisează coloanele din DataFrame pentru a le verifica
print("Coloanele disponibile în dataset:")
print(df.columns)

# Exemplu după ce alegi coloane din fisierul Pixar:
selected_columns = ['box_office_worldwide', 'rotten_tomatoes_score', 'metacritic_score', 'imdb_score']

# Creare matrice eliminand valorile lipsa
matrix = df[selected_columns].dropna().to_numpy()

#Seteaza optiunile de afisare pentru a preveni notatia stiintifica
np.set_printoptions(suppress=True)

#Afiseaza matricea
print("Matricea:")
print(matrix)

#Calcularea si afisarea: average, middle value, frequent value, range, standard deviation

#Media (Average)
average = np.mean(matrix, axis=0)

#Mediana (Middle value)
median = np.median(matrix, axis=0)

#Modul (Frequent value)
mode = stats.mode(matrix, axis=0)[0]  # Extrage doar valorile de mod

#Range (Diferenta dintre valoarea maxima si minima)
range_values = np.ptp(matrix, axis=0)

#Abaterea standard (Standard deviation)
std_dev = np.std(matrix, axis=0)

#Functie pentru a formata numărul
def format_number(val):
    if val.is_integer():  # Verificam daca valoarea este un intreg
        return f"{int(val)}"  # Afisam numarul ca intreg
    else:
        return f"{val:.2f}"  # Afisam cu 2 zecimale

#Afiseaza rezultatele cu 2 zecimale sau fara .00 dacă e intreg
print("\nStatistici pentru fiecare coloana:")
for i, col in enumerate(selected_columns):
    print(f"\nColoana: {col}")
    print(f"  Media: {format_number(average[i])}")
    print(f"  Mediana: {format_number(median[i])}")
    print(f"  Modul: {format_number(mode[i])}")
    print(f"  Range: {format_number(range_values[i])}")
    print(f"  Abaterea standard: {format_number(std_dev[i])}")

#Afisarea histograms, box plots si scatter plots

#Histograme
plt.figure(figsize=(12, 8))
for i, col in enumerate(selected_columns):
    plt.subplot(2, 3, i+1)  # Impartim figura in 2 randuri si 3 coloane
    plt.hist(df[col].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram for {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

#Box plots
plt.figure(figsize=(12, 8))
for i, col in enumerate(selected_columns):
    plt.subplot(2, 3, i+1)  # Impartim figura in 2 randuri si 3 coloane
    sns.boxplot(y=df[col].dropna(), color='lightgreen')
    plt.title(f'Box Plot for {col}')
    plt.ylabel(col)
plt.tight_layout()
plt.show()

#Scatter plots
plt.figure(figsize=(12, 8))
for i, col in enumerate(selected_columns):
    plt.subplot(2, 3, i+1)  # Impartim figura în 2 randuri și 3 coloane
    plt.scatter(df.index, df[col].dropna(), color='orange', alpha=0.6)
    plt.title(f'Scatter Plot for {col}')
    plt.xlabel('Index')
    plt.ylabel(col)
plt.tight_layout()
plt.show()

#Afisarea corelatiilor

#Calcularea corelatiilor intre coloanele numerice
correlation_matrix = df[selected_columns].corr()

#Vizualizarea corelatiilor folosind un heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
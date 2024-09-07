import pandas as pd

# Wczytanie danych z pliku CSV
data = pd.read_csv('model_results.csv')

# Znalezienie wiersza z największym mean_cv_score
best_row = data.loc[data['accuracy'].idxmax()]

# Wyświetlenie najlepszego wiersza
print("Wiersz z największym mean_cv_score:")
print(best_row)
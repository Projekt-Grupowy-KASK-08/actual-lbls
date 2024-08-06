import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from get_training_data import save_statistics_in_a_file
from itertools import product

# Wywołać raz, zeby utworzyc plik csv ze statystykami dla modelu
# save_statistics_in_a_file()

data = pd.read_csv('output_statistics.csv')
# print("\nNazwy kolumn:")
# print(data.columns)
data['label'] = data['label'].apply(lambda x: x.strip("[]").replace("'", ""))

# Rozdzielenie danych na cechy (features) i etykiety (labels)
X = data.drop(columns=['file_path', 'label'])
y = data['label']
# Zamiana etykiet stringów na numeryczne
label_encoder = LabelEncoder()
y_numerical = label_encoder.fit_transform(y)
y_string = label_encoder.classes_

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y_numerical, test_size=0.2, random_state=42)

"""
• max_depth: [80, 90, 100], maksymalna gł˛ebokos´c drzew decyzyjnych w lesie. ´
• max_features : [4, 3, 5] , liczba cech uwzgl˛ednianych przy szukaniu najlepszego rozbicia.
• min_samples_leaf : [2, 3, 4, ], minimalna liczba próbek wymagan do rozbicia liscia. ´
• min_samples_split: [6, 8, 10, 12], minimalna liczba próbek wymagana do w˛ezła w drzewie.
• n_estimators: [100, 200, 300, 500, 1000, 2000 ], liczba drzew decyzyjnych w lesie.
"""
param_grid = {
    "max_depth": [80, 90, 100],
    "max_features": [4, 3, 5],
    "min_samples_leaf": [2, 3, 4],
    "min_samples_split": [6, 8, 10, 12],
    "n_estimators": [100, 200, 300, 500, 1000, 2000]
}

# Generowanie wszystkich kombinacji
keys = param_grid.keys()
values = param_grid.values()
combinations = [dict(zip(keys, combination)) for combination in product(*values)]
results = []
# Wyświetlanie kombinacji
for combination in combinations:
    # Inicjalizacja klasyfikatora Random Forest
    clf = RandomForestClassifier(
        n_estimators=combination['n_estimators'],
        criterion='entropy',
        random_state=42,
        max_depth=combination['max_depth'],
        min_samples_split=combination['min_samples_split'],
        min_samples_leaf=combination['min_samples_leaf'],
        max_features=combination['max_features'],
    )

    # Trenowanie modelu na pełnym zbiorze treningowym
    clf.fit(X_train, y_train)

    # Dokonanie predykcji na zbiorze testowym
    y_pred = clf.predict(X_test)

    # Walidacja krzyżowa
    cv_scores = cross_val_score(clf, X, y_numerical, cv=9, scoring='accuracy')

    print(combination)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print("cross-validation score:", cv_scores)
    # Zapisanie wyników do listy
    results.append({
        'max_depth': combination['max_depth'],
        'max_features': combination['max_features'],
        'min_samples_leaf': combination['min_samples_leaf'],
        'min_samples_split': combination['min_samples_split'],
        'n_estimators': combination['n_estimators'],
        'accuracy': accuracy,
        'mean_cv_score': cv_scores.mean()
    })
# Tworzenie DataFrame z wynikami
results_df = pd.DataFrame(results)

# Zapisywanie wyników do pliku CSV
results_df.to_csv('model_results.csv', index=False)

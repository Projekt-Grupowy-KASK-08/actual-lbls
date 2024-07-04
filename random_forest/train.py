import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from get_training_data import save_statistics_in_a_file

# Wywołać raz, zeby utworzyc plik csv ze statystykami dla modelu
#save_statistics_in_a_file()

data = pd.read_csv('output_statistics.csv')
print("\nNazwy kolumn:")
print(data.columns)
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

# Inicjalizacja klasyfikatora Random Forest
clf = RandomForestClassifier(
                            n_estimators=100,
                             criterion='entropy',
                             random_state=42,
                            max_depth=5,
                            min_samples_split=2,
                            max_features='sqrt'
                             )


# Trenowanie modelu na pełnym zbiorze treningowym
clf.fit(X_train, y_train)

# Dokonanie predykcji na zbiorze testowym
y_pred = clf.predict(X_test)

# Walidacja krzyżowa
cv_scores = cross_val_score(clf, X, y_numerical, cv=9, scoring='accuracy')

# Wyświetlenie szczegółowego raportu klasyfikacji
print('Classification Report:')
print(classification_report(y_test, y_pred, zero_division=0, target_names=y_string))

# Wyświetlenie macierzy pomyłek
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

features = pd.DataFrame(clf.feature_importances_, index=X.columns)
print("\nNajważniejsze cechy:")
print(features.sort_values(by=0, ascending=False))

# Wyświetlenie wyników walidacji krzyżowej
print("Cross-validation scores:", cv_scores)
print("Mean cross-validation score:", cv_scores.mean())

# Obliczenie dokładności
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

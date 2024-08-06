import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from get_training_data import save_statistics_in_a_file
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import joblib

# Wywołać raz, zeby utworzyc plik csv ze statystykami dla modelu
# argumentem jest czas analizowanego sygnału w sekundach
save_statistics_in_a_file(1/8)

"""data = pd.read_csv('output_statistics.csv')
print(data)
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
X_train, X_test, y_train, y_test = train_test_split(X, y_numerical, test_size=0.15)

# Inicjalizacja klasyfikatora Random Forest
clf = RandomForestClassifier(
    n_estimators=500,
    criterion='entropy',
    max_depth=80,
    min_samples_split=6,
    min_samples_leaf=3,
    max_features=10,
    random_state=42
)

# Trenowanie modelu na pełnym zbiorze treningowym
clf.fit(X_train, y_train)

# Zapisanie modelu do pliku
joblib.dump(clf, 'random_forest_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

# Dokonanie predykcji na zbiorze testowym
y_pred = clf.predict(X_test)
# Obliczenie dokładności
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Walidacja krzyżowa
print("performing cross validation")
cv_scores = cross_val_score(clf, X, y_numerical, cv=9, scoring='accuracy')
print("Cross-validation scores:", cv_scores)
print("Mean cross-validation score:", cv_scores.mean())

# Wyświetlenie szczegółowego raportu klasyfikacji
print('Classification Report:')
print(classification_report(y_test, y_pred, zero_division=0, target_names=y_string))

# Wyświetlenie macierzy pomyłek
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

features = pd.DataFrame(clf.feature_importances_, index=X.columns)
print("\nNajważniejsze cechy i ich wagi:")
print(features.sort_values(by=0, ascending=False))

# Wizualizacja jednego z drzew i zapis do pliku
plt.figure(figsize=(10, 5))  # Dostosuj rozmiar figury
plot_tree(clf.estimators_[0],
          feature_names=X.columns,
          class_names=label_encoder.classes_,
          filled=True,
          rounded=True,
          proportion=True,
          fontsize=2)
plt.savefig('tree_visualization.png', format='png', dpi=300)"""

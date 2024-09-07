import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from get_training_data import save_statistics_in_a_file
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import joblib

# Wywołać raz, aby utworzyć plik CSV ze statystykami dla modelu
# argumentem jest czas analizowanego sygnału w sekundach
#save_statistics_in_a_file(1)

# Wczytanie danych z pliku CSV
data = pd.read_csv('output_statistics.csv')
print("\nNazwy kolumn:")
print(data.columns)
data['label'] = data['label'].apply(lambda x: x.strip("[]").replace("'", ""))

# Rozdzielenie danych na cechy (features) i etykiety (labels)
X = data.drop(columns=['file_path', 'label'])
y = data['label']

# Zamiana etykiet stringów na wartości numeryczne
label_encoder = LabelEncoder()
y_numerical = label_encoder.fit_transform(y)
y_string = label_encoder.classes_
shortened_classes = [
    'Czesci wewnetrzne' if 'Czesci wewnetrzne galki bladej' in name else
    'Czesci zewnetrzne' if 'Czesci zewnetrzne galki bladej' in name else name
    for name in label_encoder.classes_
]

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y_numerical, test_size=0.2)

# Obliczenie liczby wierszy dla każdej z klas w zbiorze treningowym i testowym
y_train_counts = pd.Series(y_train).value_counts()
y_test_counts = pd.Series(y_test).value_counts()
mapping = {i: shortened_classes[i] for i in range(len(shortened_classes))}

# Zamiana numerycznych etykiet na skrócone nazwy klas w y_train_counts
y_train_counts_named = y_train_counts.rename(index=mapping)
y_test_counts_named = y_test_counts.rename(index=mapping)

# Wyświetlenie liczby wierszy dla każdej z klas w zbiorze treningowym
print("Liczba wierszy każdej z klas w y_train:")
print(y_train_counts_named)

# Wyświetlenie liczby wierszy dla każdej z klas w zbiorze testowym
print("\nLiczba wierszy każdej z klas w y_test:")
print(y_test_counts_named)

# Inicjalizacja klasyfikatora Random Forest
clf = RandomForestClassifier(
    n_estimators=25,
    criterion='gini',
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
print(f'Dokładność: {accuracy}')

# Walidacja krzyżowa
print("Przeprowadzanie walidacji krzyżowej")
cv_scores = cross_val_score(clf, X, y_numerical, cv=9, scoring='accuracy')
print("Wyniki walidacji krzyżowej:", cv_scores)
print("Średni wynik walidacji krzyżowej:", cv_scores.mean())

# Wyświetlenie szczegółowego raportu klasyfikacji
print('Raport klasyfikacji:')
print(classification_report(y_test, y_pred, zero_division=0, target_names=y_string))

# Wyświetlenie macierzy pomyłek
cm = confusion_matrix(y_test, y_pred)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# Tworzenie DataFrame z macierzy pomyłek ze skróconymi nazwami klas
cm_df = pd.DataFrame(cm, index=shortened_classes, columns=shortened_classes)
print('Macierz pomyłek:')
print('(rzeczywiste klasy w wierszach, przewidziane klasy w kolumnach)')
print(cm_df)

# Wyświetlenie najważniejszych cech i ich wag
features = pd.DataFrame(clf.feature_importances_, index=X.columns)
print("\nNajważniejsze cechy i ich wagi:")
print(features.sort_values(by=0, ascending=False))

# Wizualizacja jednego z drzew i zapis do pliku
plt.figure(figsize=(10, 5))
plot_tree(clf.estimators_[0],
          feature_names=X.columns,
          class_names=label_encoder.classes_,
          filled=True,
          rounded=True,
          proportion=True,
          fontsize=2)
plt.savefig('tree_visualization.png', format='png', dpi=300)

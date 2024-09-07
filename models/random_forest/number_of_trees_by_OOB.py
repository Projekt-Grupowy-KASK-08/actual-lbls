import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

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


# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y_numerical, test_size=0.2)

# Inicjalizacja pustych list do przechowywania liczby drzew i odpowiadających im wskaźników błędu OOB
oob_errors = []
n_estimators_range = range(1, 201)  # Zakres liczby drzew od 1 do 200

# Przeprowadzanie pętli, aby trenować model z różną liczbą drzew
for n_estimators in n_estimators_range:
    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        oob_score=True,  # Włączanie OOB score
        criterion='gini',
        max_depth=80,
        min_samples_split=6,
        min_samples_leaf=3,
        max_features=10,
        random_state=42
    )
    clf.fit(X_train, y_train)

    # Dodawanie wskaźnika błędu OOB do listy
    oob_error = 1 - clf.oob_score_
    oob_errors.append(oob_error)

# Krok 2: Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.plot(n_estimators_range, oob_errors, label='OOB Error Rate', color='blue')
plt.xlabel('Number of Decision Trees')
plt.ylabel('OOB Error Rate')
plt.title('Number of Decision Trees and OOB Error Rate Curve')
plt.axvline(x=100, color='red', linestyle='--', label='100 Trees')
plt.legend()
plt.grid(True)
plt.show()

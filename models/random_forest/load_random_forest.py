import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split, cross_val_score

# Wczytanie modelu i enkodera etykiet
clf = joblib.load('random_forest_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

data = pd.read_csv('output_statistics.csv')

data['label'] = data['label'].apply(lambda x: x.strip("[]").replace("'", ""))

# Rozdzielenie danych na cechy (features) i etykiety (labels)
X = data.drop(columns=['file_path', 'label'])
y = data['label']

# Zamiana etykiet stringów na numeryczne
y_numerical = label_encoder.transform(y)
y_string = label_encoder.classes_

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y_numerical, test_size=1)

print("predicting")
# Dokonanie predykcji na zbiorze testowym
y_pred = clf.predict(X_test)
# Obliczenie dokładności
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')


features = pd.DataFrame(clf.feature_importances_, index=X.columns)
print("\nNajważniejsze cechy:")
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
plt.show()

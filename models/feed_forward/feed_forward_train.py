import joblib
import keras.optimizers
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import np_utils
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Wczytanie danych
data_f = pd.read_csv('../random_forest/output_statistics.csv')

from sklearn.preprocessing import StandardScaler

# Wybór kolumn numerycznych do normalizacji
numeric_columns = data_f.select_dtypes(include=['float64', 'int64']).columns

# Stworzenie kopii danych, aby zachować oryginalne dane nienaruszone
data_normalized = data_f.copy()

# Normalizacja kolumn numerycznych
scaler = StandardScaler()
data_normalized[numeric_columns] = scaler.fit_transform(data_f[numeric_columns])

data = data_normalized
data = data.dropna()
data['label'] = data['label'].apply(lambda x: x.strip("[]").replace("'", ""))

# Rozdzielenie danych na cechy (features) i etykiety (labels)
X = data.drop(columns=['file_path', 'label'])
y = data['label']

# Zamiana etykiet stringów na numeryczne
label_encoder = LabelEncoder()
y_numerical = label_encoder.fit_transform(y)
y_string = label_encoder.classes_

# Konwersja etykiet do postaci one-hot
y_categorical = np_utils.to_categorical(y_numerical)

# Próbkowanie nadmiarowe (Oversampling) za pomocą SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y_numerical)
y_resampled_categorical = np_utils.to_categorical(y_resampled)

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled_categorical, test_size=0.1, random_state=42)

# Definicja modelu feedforward
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
#model.add(Dense(16, activation='relu'))
model.add(Dense(len(y_string), activation='softmax'))

# Obliczenie wag klasowych
class_weights = {i: max(y_resampled) / np.sum(y_resampled == i) for i in np.unique(y_resampled)}

# Kompilacja modelu z ważoną funkcją straty
model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adam(lr=0.01), metrics=['accuracy'])

# Trenowanie modelu
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.5, verbose=2, class_weight=class_weights)

# Zapisanie modelu do pliku
model.save('feedforward_model_balanced.h5')
joblib.dump(label_encoder, 'label_encoder_nn_balanced.pkl')

# Dokonanie predykcji na zbiorze testowym
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_test_classes = np.argmax(y_test, axis=1)

# Obliczenie dokładności
accuracy = accuracy_score(y_test_classes, y_pred_classes)
print(f'Accuracy: {accuracy}')

# Wyświetlenie szczegółowego raportu klasyfikacji
print('Classification Report:')
print(classification_report(y_test_classes, y_pred_classes, target_names=y_string))

# Wyświetlenie macierzy pomyłek
print('Confusion Matrix:')
print(confusion_matrix(y_test_classes, y_pred_classes))

# Wizualizacja historii treningu
plt.figure(figsize=(12, 5))

# Wizualizacja dokładności
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Wizualizacja straty
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig('training_history_balanced.png', format='png', dpi=300)
plt.show()

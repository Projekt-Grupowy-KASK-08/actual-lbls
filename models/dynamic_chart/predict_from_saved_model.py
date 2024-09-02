import joblib
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

from models.dynamic_chart.calculate_statistics_from_array import calculate_statistics_from_array


def predict_from_saved_model(array, depth):
    # Load the saved model
    model = load_model('/Users/pawelmanczak/PG sem 5/actual-lbls/models/feed_forward/feedforward_model_balanced.h5')

    # Load the label encoder
    label_encoder = joblib.load(
        '/Users/pawelmanczak/PG sem 5/actual-lbls/models/feed_forward/label_encoder_nn_balanced.pkl')

    # Load and preprocess new data (ensure it has the same structure as the training data)
    new_data = calculate_statistics_from_array(array, depth=depth)

    # Normalization
    scaler = StandardScaler()
    new_data_normalized = scaler.fit_transform(new_data)

    # Making predictions
    predictions = model.predict(new_data_normalized)

    # Convert predictions to class labels
    predicted_classes = np.argmax(predictions, axis=1)
    predicted_labels = label_encoder.inverse_transform(predicted_classes)
    return predicted_labels


"""
def randomDataFrameOfFloats(size):
    return pd.DataFrame(np.random.randn(size))
    
input_data = np.random.randn(1500)

# Convert numpy array to pandas DataFrame
df_input_data = pd.DataFrame(input_data, columns=['Data'])
df_statistics = calculate_statistics_from_array(input_data=df_input_data['Data'], depth=-1)
print(df_statistics)

print(predictFromSavedModel(df_input_data['Data']))
"""

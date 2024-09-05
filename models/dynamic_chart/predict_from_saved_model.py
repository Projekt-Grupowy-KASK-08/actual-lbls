import joblib
import numpy as np
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

from models.dynamic_chart.calculate_statistics_from_array import calculate_statistics_from_array

MODEL_PATH = '/Users/pawelmanczak/PG sem 5/actual-lbls/models/random_forest/random_forest_model.pkl'
LABEL_ENCODER_PATH = '/Users/pawelmanczak/PG sem 5/actual-lbls/models/random_forest/label_encoder.pkl'
MODEL_TYPE = 'random_forest'  # 'random_forest' or 'feed_forward'


def predict_from_saved_model(array, depth, model_type=MODEL_TYPE, model_path=MODEL_PATH,
                             label_encoder_path=LABEL_ENCODER_PATH):
    """
      This function performs predictions using the selected model (either Random Forest or Feedforward Neural Network).

      :param array: Input data for predictions (e.g., raw data to be processed)
      :param depth: Depth parameter (used in the calculate_statistics_from_array function)
      :param model_type: Type of model to use ('random_forest' or 'neural_network')
      :param model_path: Path to the saved model file
      :param label_encoder_path: Path to the label encoder file
      :return: Returns predicted labels
      """
    if model_type == 'random_forest':
        clf = joblib.load(model_path)
        label_encoder = joblib.load(label_encoder_path)

        df_input_data = pd.DataFrame(array, columns=['Data'])
        df_statistics = calculate_statistics_from_array(input_data=df_input_data['Data'], depth=depth)

        predictions = clf.predict(df_statistics)
        predicted_labels = label_encoder.inverse_transform(predictions)

    elif model_type == 'neural_network':
        model = load_model(model_path)
        label_encoder = joblib.load(label_encoder_path)

        new_data = calculate_statistics_from_array(array, depth=depth)

        scaler = StandardScaler()
        new_data_normalized = scaler.fit_transform(new_data)

        predictions = model.predict(new_data_normalized)
        predicted_classes = np.argmax(predictions, axis=1)
        predicted_labels = label_encoder.inverse_transform(predicted_classes)

    else:
        raise ValueError("Wrong model type")

    return predicted_labels


"""
def randomDataFrameOfFloats(size):
    return pd.DataFrame(np.random.randn(size))



# Convert numpy array to pandas DataFrame
df_input_data = pd.DataFrame(input_data, columns=['Data'])
df_statistics = calculate_statistics_from_array(input_data=df_input_data['Data'], depth=-1)
print(df_statistics)

print(predictFromSavedModel(df_input_data['Data']))
"""

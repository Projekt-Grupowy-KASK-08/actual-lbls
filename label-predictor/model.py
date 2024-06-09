from typing import List, Dict, Optional
from label_studio_ml.model import LabelStudioMLBase
from label_studio_ml.response import ModelResponse
import pandas as pd

from classifier_logic import classify


class NewModel(LabelStudioMLBase):
    """Custom ML Backend model
    """

    def setup(self):
        """Configure any parameters of your model here
        """
        self.set("model_version", "0.0.1")

    def predict(self, tasks: List[Dict], context: Optional[Dict] = None, **kwargs) -> ModelResponse:
        """ Write your inference logic here
            :param tasks: [Label Studio tasks in JSON format](https://labelstud.io/guide/task_format.html)
            :param context: [Label Studio context in JSON format](https://labelstud.io/guide/ml_create#Implement-prediction-logic)
            :return model_response
                ModelResponse(predictions=predictions) with
                predictions: [Predictions array in JSON format](https://labelstud.io/guide/export.html#Label-Studio-JSON-format-of-annotated-tasks)
        """
        print(f'''\
        Run prediction on {tasks}
        Received context: {context}
        Project ID: {self.project_id}
        Label config: {self.label_config}
        Parsed JSON Label config: {self.parsed_label_config}
        Extra params: {self.extra_params}''')

        predictions = []
        for task in tasks:
            csv_url = task['data']['csv']
            url = csv_url.replace(' ', '%20').replace('http://localhost/dbs/static/', 'https://kask.eti.pg.edu.pl/dbs/static/preprocessed/')
            print(url)
            try:
                data = pd.read_csv(url)
            except Exception as e:
                print(url)
                print(f"Błąd wczytywania danych: {e}")
 
            if data is None:
                predictions.append({})
            else:
                start, end = classify(data, 1000)
                predictions.append({
                    "model_version": self.get("model_version"),
                    "score": 1.0,
                    "result": [{
                        "id": "test",
                        "from_name": "label",
                        "to_name": "ts",
                        "type": "timeserieslabels",
                        "value": {
                            "start": start,
                            "end": end,
                            "instant": False,
                            "timeserieslabels": ["Skorupa lub prazkowie"]
                        }
                    }]
                })

        return predictions

    def fit(self, event, data, **kwargs):
        """
        This method is called each time an annotation is created or updated
        You can run your logic here to update the model and persist it to the cache
        It is not recommended to perform long-running operations here, as it will block the main thread
        Instead, consider running a separate process or a thread (like RQ worker) to perform the training
        :param event: event type can be ('ANNOTATION_CREATED', 'ANNOTATION_UPDATED', 'START_TRAINING')
        :param data: the payload received from the event (check [Webhook event reference](https://labelstud.io/guide/webhook_reference.html))
        """

        # use cache to retrieve the data from the previous fit() runs
        old_data = self.get('my_data')
        old_model_version = self.get('model_version')
        print(f'Old data: {old_data}')
        print(f'Old model version: {old_model_version}')

        # store new data to the cache
        self.set('my_data', 'my_new_data_value')
        self.set('model_version', 'my_new_model_version')
        print(f'New data: {self.get("my_data")}')
        print(f'New model version: {self.get("model_version")}')

        print('fit() completed successfully.')

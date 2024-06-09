"""
This file contains tests for the API of your model. You can run these tests by installing test requirements:

    ```bash
    pip install -r requirements-test.txt
    ```
Then execute `pytest` in the directory of this file.

- Change `NewModel` to the name of the class in your model.py file.
- Change the `request` and `expected_response` variables to match the input and output of your model.
"""

import pytest
import json
from model import NewModel


@pytest.fixture
def client():
    from _wsgi import init_app
    app = init_app(model_class=NewModel)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict(client):
    request = {
        'tasks': [{'id': 173, 'data': {'csv': 'http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-0,5_kanalAnterior.csv', 'text': 'Depth: -0,5 mm  Channel: Anterior'}, 'meta': {}, 'created_at': '2024-06-08T10:05:40.277462Z', 'updated_at': '2024-06-08T10:05:40.277505Z', 'is_labeled': False, 'overlap': 1, 'inner_id': 1, 'total_annotations': 0, 'cancelled_annotations': 0, 'total_predictions': 0, 'comment_count': 0, 'unresolved_comment_count': 0, 'last_comment_updated_at': None, 'project': 6, 'updated_by': None, 'file_upload': None, 'comment_authors': [], 'annotations': [], 'predictions': []}],
        # Your labeling configuration here
        "label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"true\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>"
    }


    expected_response = {
        'results': [{
            # Your expected result here
        }]
    }

    response = client.post('/predict', data=json.dumps(request), content_type='application/json')
    assert response.status_code == 200
    response = json.loads(response.data)
    print(response)
   # assert response == expected_response

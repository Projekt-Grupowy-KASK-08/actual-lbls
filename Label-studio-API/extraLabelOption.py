import requests

# Ustawienia API Label Studio
API_URL = "http://localhost/dbs/labels/"
API_TOKEN = "37d89764f7e10553bcde81af78b39f6ebea45d12"

# Zakres ID projektów
START_ID = 13
END_ID = 18

# Nowy interfejs etykietowania
LABELING_INTERFACE = """<View> <Header size="4" underline="true" value="$name"/> <TimeSeries name="ts" valueType="url" value="$csv" sep="," overviewWidth="1%" timeColumn="Time"> <Channel column="1: Raw" strokeColor="#17b" legend="Raw" units="Activity" fixedScale="false"/> <Channel column="2: Preprocessed" strokeColor="#f70" legend="Preprocessed" units="Activity" fixedScale="false"/> </TimeSeries> <TimeSeriesLabels name="label" toName="ts"> <Label value="Skorupa lub prazkowie" background="#80ff00"/> <Label value="Czesci zewnetrzne galki bladej (5-6 mm przed celem)" background="#D4380D"/> <Label value="Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)" background="#FFC069"/> <Label value="Czysty fragment" background="#969696"/></TimeSeriesLabels> </View>"""

print(LABELING_INTERFACE)
# Nagłówki żądania
headers = {
    'Authorization': f'Token {API_TOKEN}',
    'Content-Type': 'application/json'
}

# Funkcja aktualizująca interfejs etykietowania dla projektu
def update_project_labeling_interface(project_id):
    url = f"{API_URL}/{project_id}"
    data = {
        "label_config": LABELING_INTERFACE
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Project {project_id} updated successfully.")
    else:
        print(f"Failed to update project {project_id}. Status code: {response.status_code}, Response: {response.text}")

# Iteracja przez zakres ID projektów i aktualizacja każdego z nich
for project_id in range(START_ID, END_ID + 1):
    update_project_labeling_interface(project_id)

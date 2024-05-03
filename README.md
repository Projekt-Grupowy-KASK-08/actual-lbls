# actual-lbls

### Data preparation
To prepare data, please install dependencies, put proper MER data in the `data/raw/` directory and run the script.
```
cd parser
pip install -r requirements.txt
python3 data_transformer.py
```
Preprocessed data will show up in the `data/preprocessed` directory.
Configuration (e.g. directory settings) is contained in first lines of `data_transformer.py`.  

### Running application via docker-compose
To serve the app, run 
```sh
docker compose up
```
Label studio will be available on port 8080 and http server with files on port 8787

### Serving data
We use a static web server to serve labeling data to client. To upload your data, simply move it to [data directory](./http-server/data)

### URLs
To create projects and import data you need to set up few variables inside `LabelStudioAPI.py`. Firstly `TOKEN` which value can be found in label studio settings. `PROJECT_ID_OFFSET` id of lastly created project in your label studio account (last project is on top-left corner). You can find it in url path http://localhost:8080/projects/2/data?tab=1 in this case it's 2. Also make sure that `INPUT_DIR`, `OUTPUT_DIR`, `FILE_SERVER_URL` and `LABEL_STUDIO_URL` are correct. Run LabelStudioApi.py. Open console in `OUTPUT_DIR` and run `bash CreateProjects.sh`.

# actual-lbls

## Running application via docker-compose
To serve the app, run 
```sh
docker compose up
```
Label studio will be available on port 8080 and http server with files on port 8787

## Serving data
We use a static web server to serve labeling data to client. To upload your data, simply move it to [data directory](./http-server/data)

### URLs
To import tasks via `.json` file, you have to specify a backend-relative url to the file (so instead of `localhost:8787/tasks.json`, it will be `http://http-server:8787/tasks.json`). The json file has to specify client-relative url, eg. `localhost:8787/data1.csv`

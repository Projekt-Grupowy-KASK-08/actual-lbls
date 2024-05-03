curl -v -k -H Content-Type:application/json -H 'Authorization: Token 1c0d537815c777dd0394938b9b1a6c849cb5de84' -X POST 'https://kask.eti.pg.edu.pl/dbs/labels//api/projects' --data '{ 
"title": "Adamczyk Tadeusz 2018-10-25",
"label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"true\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>",
"sampling": "Sequential sampling"
}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token 1c0d537815c777dd0394938b9b1a6c849cb5de84' -X POST 'https://kask.eti.pg.edu.pl/dbs/labels//api/projects/1311/import' -d '[
{
"id": 1,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-10,0_kanalCentral.csv","text": "Depth: -10,0 mm  Channel: Central"}
},
{
"id": 2,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-10,0_kanalLateral.csv","text": "Depth: -10,0 mm  Channel: Lateral"}
},
{
"id": 3,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-9,7_kanalCentral.csv","text": "Depth: -9,7 mm  Channel: Central"}
},
{
"id": 4,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-9,7_kanalLateral.csv","text": "Depth: -9,7 mm  Channel: Lateral"}
},
{
"id": 5,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-9,4_kanalCentral.csv","text": "Depth: -9,4 mm  Channel: Central"}
},
{
"id": 6,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-9,4_kanalLateral.csv","text": "Depth: -9,4 mm  Channel: Lateral"}
},
{
"id": 7,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-9,1_kanalCentral.csv","text": "Depth: -9,1 mm  Channel: Central"}
},
{
"id": 8,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-9,1_kanalLateral.csv","text": "Depth: -9,1 mm  Channel: Lateral"}
},
{
"id": 9,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-8,8_kanalCentral.csv","text": "Depth: -8,8 mm  Channel: Central"}
},
{
"id": 10,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-8,8_kanalLateral.csv","text": "Depth: -8,8 mm  Channel: Lateral"}
},
{
"id": 11,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-8,5_kanalCentral.csv","text": "Depth: -8,5 mm  Channel: Central"}
},
{
"id": 12,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-8,5_kanalLateral.csv","text": "Depth: -8,5 mm  Channel: Lateral"}
},
{
"id": 13,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-8,2_kanalCentral.csv","text": "Depth: -8,2 mm  Channel: Central"}
},
{
"id": 14,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-8,2_kanalLateral.csv","text": "Depth: -8,2 mm  Channel: Lateral"}
},
{
"id": 15,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,9_kanalCentral.csv","text": "Depth: -7,9 mm  Channel: Central"}
},
{
"id": 16,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,9_kanalLateral.csv","text": "Depth: -7,9 mm  Channel: Lateral"}
},
{
"id": 17,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,6_kanalCentral.csv","text": "Depth: -7,6 mm  Channel: Central"}
},
{
"id": 18,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,6_kanalLateral.csv","text": "Depth: -7,6 mm  Channel: Lateral"}
},
{
"id": 19,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,3_kanalCentral.csv","text": "Depth: -7,3 mm  Channel: Central"}
},
{
"id": 20,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,3_kanalLateral.csv","text": "Depth: -7,3 mm  Channel: Lateral"}
},
{
"id": 21,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,0_kanalCentral.csv","text": "Depth: -7,0 mm  Channel: Central"}
},
{
"id": 22,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-7,0_kanalLateral.csv","text": "Depth: -7,0 mm  Channel: Lateral"}
},
{
"id": 23,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-6,7_kanalCentral.csv","text": "Depth: -6,7 mm  Channel: Central"}
},
{
"id": 24,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-6,7_kanalLateral.csv","text": "Depth: -6,7 mm  Channel: Lateral"}
},
{
"id": 25,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-6,4_kanalCentral.csv","text": "Depth: -6,4 mm  Channel: Central"}
},
{
"id": 26,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-6,4_kanalLateral.csv","text": "Depth: -6,4 mm  Channel: Lateral"}
},
{
"id": 27,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-6,1_kanalCentral.csv","text": "Depth: -6,1 mm  Channel: Central"}
},
{
"id": 28,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-6,1_kanalLateral.csv","text": "Depth: -6,1 mm  Channel: Lateral"}
},
{
"id": 29,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-5,8_kanalCentral.csv","text": "Depth: -5,8 mm  Channel: Central"}
},
{
"id": 30,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-5,8_kanalLateral.csv","text": "Depth: -5,8 mm  Channel: Lateral"}
},
{
"id": 31,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-5,5_kanalCentral.csv","text": "Depth: -5,5 mm  Channel: Central"}
},
{
"id": 32,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-5,5_kanalLateral.csv","text": "Depth: -5,5 mm  Channel: Lateral"}
},
{
"id": 33,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-5,2_kanalCentral.csv","text": "Depth: -5,2 mm  Channel: Central"}
},
{
"id": 34,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-5,2_kanalLateral.csv","text": "Depth: -5,2 mm  Channel: Lateral"}
},
{
"id": 35,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-4,9_kanalCentral.csv","text": "Depth: -4,9 mm  Channel: Central"}
},
{
"id": 36,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-4,9_kanalLateral.csv","text": "Depth: -4,9 mm  Channel: Lateral"}
},
{
"id": 37,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-4,6_kanalCentral.csv","text": "Depth: -4,6 mm  Channel: Central"}
},
{
"id": 38,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-4,6_kanalLateral.csv","text": "Depth: -4,6 mm  Channel: Lateral"}
},
{
"id": 39,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-4,3_kanalCentral.csv","text": "Depth: -4,3 mm  Channel: Central"}
},
{
"id": 40,
"data": {"csv": "https://kask.eti.pg.edu.pl/dbs/static/preprocessed//Adamczyk Tadeusz/530614040/depth-4,3_kanalLateral.csv","text": "Depth: -4,3 mm  Channel: Lateral"}
}
]'
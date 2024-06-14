curl -v -k -H Content-Type:application/json -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects' --data '{ 
"title": "Sloma Pawel 2016-10-12",
"label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"false\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>",
"sampling": "Sequential sampling"
}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects/1/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-10,0_kanalCentral.csv","text": "Depth: -10,0 mm  Channel: Central"}
},
{
"id": 2,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-10,0_kanalLateral.csv","text": "Depth: -10,0 mm  Channel: Lateral"}
},
{
"id": 3,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-4,6_kanalCentral.csv","text": "Depth: -4,6 mm  Channel: Central"}
},
{
"id": 4,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-4,6_kanalLateral.csv","text": "Depth: -4,6 mm  Channel: Lateral"}
},
{
"id": 5,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-4,9_kanalCentral.csv","text": "Depth: -4,9 mm  Channel: Central"}
},
{
"id": 6,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-4,9_kanalLateral.csv","text": "Depth: -4,9 mm  Channel: Lateral"}
},
{
"id": 7,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-5,2_kanalCentral.csv","text": "Depth: -5,2 mm  Channel: Central"}
},
{
"id": 8,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-5,2_kanalLateral.csv","text": "Depth: -5,2 mm  Channel: Lateral"}
},
{
"id": 9,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-5,5_kanalCentral.csv","text": "Depth: -5,5 mm  Channel: Central"}
},
{
"id": 10,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-5,5_kanalLateral.csv","text": "Depth: -5,5 mm  Channel: Lateral"}
},
{
"id": 11,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-5,8_kanalCentral.csv","text": "Depth: -5,8 mm  Channel: Central"}
},
{
"id": 12,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-5,8_kanalLateral.csv","text": "Depth: -5,8 mm  Channel: Lateral"}
},
{
"id": 13,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-6,1_kanalCentral.csv","text": "Depth: -6,1 mm  Channel: Central"}
},
{
"id": 14,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-6,1_kanalLateral.csv","text": "Depth: -6,1 mm  Channel: Lateral"}
},
{
"id": 15,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-6,4_kanalCentral.csv","text": "Depth: -6,4 mm  Channel: Central"}
},
{
"id": 16,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-6,4_kanalLateral.csv","text": "Depth: -6,4 mm  Channel: Lateral"}
},
{
"id": 17,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-6,7_kanalCentral.csv","text": "Depth: -6,7 mm  Channel: Central"}
},
{
"id": 18,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-6,7_kanalLateral.csv","text": "Depth: -6,7 mm  Channel: Lateral"}
},
{
"id": 19,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,0_kanalCentral.csv","text": "Depth: -7,0 mm  Channel: Central"}
},
{
"id": 20,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,0_kanalLateral.csv","text": "Depth: -7,0 mm  Channel: Lateral"}
},
{
"id": 21,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,3_kanalCentral.csv","text": "Depth: -7,3 mm  Channel: Central"}
},
{
"id": 22,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,3_kanalLateral.csv","text": "Depth: -7,3 mm  Channel: Lateral"}
},
{
"id": 23,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,6_kanalCentral.csv","text": "Depth: -7,6 mm  Channel: Central"}
},
{
"id": 24,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,6_kanalLateral.csv","text": "Depth: -7,6 mm  Channel: Lateral"}
},
{
"id": 25,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,9_kanalCentral.csv","text": "Depth: -7,9 mm  Channel: Central"}
},
{
"id": 26,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-7,9_kanalLateral.csv","text": "Depth: -7,9 mm  Channel: Lateral"}
},
{
"id": 27,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-8,2_kanalCentral.csv","text": "Depth: -8,2 mm  Channel: Central"}
},
{
"id": 28,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-8,2_kanalLateral.csv","text": "Depth: -8,2 mm  Channel: Lateral"}
},
{
"id": 29,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-8,5_kanalCentral.csv","text": "Depth: -8,5 mm  Channel: Central"}
},
{
"id": 30,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-8,5_kanalLateral.csv","text": "Depth: -8,5 mm  Channel: Lateral"}
},
{
"id": 31,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-8,8_kanalCentral.csv","text": "Depth: -8,8 mm  Channel: Central"}
},
{
"id": 32,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-8,8_kanalLateral.csv","text": "Depth: -8,8 mm  Channel: Lateral"}
},
{
"id": 33,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-9,1_kanalCentral.csv","text": "Depth: -9,1 mm  Channel: Central"}
},
{
"id": 34,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-9,1_kanalLateral.csv","text": "Depth: -9,1 mm  Channel: Lateral"}
},
{
"id": 35,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-9,4_kanalCentral.csv","text": "Depth: -9,4 mm  Channel: Central"}
},
{
"id": 36,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-9,4_kanalLateral.csv","text": "Depth: -9,4 mm  Channel: Lateral"}
},
{
"id": 37,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-9,7_kanalCentral.csv","text": "Depth: -9,7 mm  Channel: Central"}
},
{
"id": 38,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466417777/depth-9,7_kanalLateral.csv","text": "Depth: -9,7 mm  Channel: Lateral"}
}
]'

curl -v -k -H Content-Type:application/json -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects' --data '{ 
"title": "Sloma Pawel 2016-10-12",
"label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"false\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>",
"sampling": "Sequential sampling"
}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects/2/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-10,0_kanalCentral.csv","text": "Depth: -10,0 mm  Channel: Central"}
},
{
"id": 2,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-10,0_kanalLateral.csv","text": "Depth: -10,0 mm  Channel: Lateral"}
},
{
"id": 3,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-5,5_kanalCentral.csv","text": "Depth: -5,5 mm  Channel: Central"}
},
{
"id": 4,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-5,5_kanalLateral.csv","text": "Depth: -5,5 mm  Channel: Lateral"}
},
{
"id": 5,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-5,8_kanalCentral.csv","text": "Depth: -5,8 mm  Channel: Central"}
},
{
"id": 6,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-5,8_kanalLateral.csv","text": "Depth: -5,8 mm  Channel: Lateral"}
},
{
"id": 7,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-6,1_kanalCentral.csv","text": "Depth: -6,1 mm  Channel: Central"}
},
{
"id": 8,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-6,1_kanalLateral.csv","text": "Depth: -6,1 mm  Channel: Lateral"}
},
{
"id": 9,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-6,4_kanalCentral.csv","text": "Depth: -6,4 mm  Channel: Central"}
},
{
"id": 10,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-6,4_kanalLateral.csv","text": "Depth: -6,4 mm  Channel: Lateral"}
},
{
"id": 11,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-6,7_kanalCentral.csv","text": "Depth: -6,7 mm  Channel: Central"}
},
{
"id": 12,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-6,7_kanalLateral.csv","text": "Depth: -6,7 mm  Channel: Lateral"}
},
{
"id": 13,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,0_kanalCentral.csv","text": "Depth: -7,0 mm  Channel: Central"}
},
{
"id": 14,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,0_kanalLateral.csv","text": "Depth: -7,0 mm  Channel: Lateral"}
},
{
"id": 15,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,3_kanalCentral.csv","text": "Depth: -7,3 mm  Channel: Central"}
},
{
"id": 16,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,3_kanalLateral.csv","text": "Depth: -7,3 mm  Channel: Lateral"}
},
{
"id": 17,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,6_kanalCentral.csv","text": "Depth: -7,6 mm  Channel: Central"}
},
{
"id": 18,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,6_kanalLateral.csv","text": "Depth: -7,6 mm  Channel: Lateral"}
},
{
"id": 19,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,9_kanalCentral.csv","text": "Depth: -7,9 mm  Channel: Central"}
},
{
"id": 20,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-7,9_kanalLateral.csv","text": "Depth: -7,9 mm  Channel: Lateral"}
},
{
"id": 21,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-8,2_kanalCentral.csv","text": "Depth: -8,2 mm  Channel: Central"}
},
{
"id": 22,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-8,2_kanalLateral.csv","text": "Depth: -8,2 mm  Channel: Lateral"}
},
{
"id": 23,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-8,5_kanalCentral.csv","text": "Depth: -8,5 mm  Channel: Central"}
},
{
"id": 24,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-8,5_kanalLateral.csv","text": "Depth: -8,5 mm  Channel: Lateral"}
},
{
"id": 25,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-8,8_kanalCentral.csv","text": "Depth: -8,8 mm  Channel: Central"}
},
{
"id": 26,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-8,8_kanalLateral.csv","text": "Depth: -8,8 mm  Channel: Lateral"}
},
{
"id": 27,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-9,1_kanalCentral.csv","text": "Depth: -9,1 mm  Channel: Central"}
},
{
"id": 28,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-9,1_kanalLateral.csv","text": "Depth: -9,1 mm  Channel: Lateral"}
},
{
"id": 29,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-9,4_kanalCentral.csv","text": "Depth: -9,4 mm  Channel: Central"}
},
{
"id": 30,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-9,4_kanalLateral.csv","text": "Depth: -9,4 mm  Channel: Lateral"}
},
{
"id": 31,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-9,7_kanalCentral.csv","text": "Depth: -9,7 mm  Channel: Central"}
},
{
"id": 32,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466423569/depth-9,7_kanalLateral.csv","text": "Depth: -9,7 mm  Channel: Lateral"}
}
]'

curl -v -k -H Content-Type:application/json -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects' --data '{ 
"title": "Sloma Pawel 2016-10-12",
"label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"false\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>",
"sampling": "Sequential sampling"
}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects/3/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466427039/depth-10,0_kanal3Anterior.csv","text": "Depth: -10,0 mm  Channel: 3Anterior"}
},
{
"id": 2,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466427039/depth-10,0_kanalCentral.csv","text": "Depth: -10,0 mm  Channel: Central"}
},
{
"id": 3,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466427039/depth-10,0_kanalLateral.csv","text": "Depth: -10,0 mm  Channel: Lateral"}
},
{
"id": 4,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466427039/depth-9,7_kanal3Anterior.csv","text": "Depth: -9,7 mm  Channel: 3Anterior"}
},
{
"id": 5,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466427039/depth-9,7_kanalCentral.csv","text": "Depth: -9,7 mm  Channel: Central"}
},
{
"id": 6,
"data": {"csv": "http://localhost/dbs/static//Sloma Pawel/466427039/depth-9,7_kanalLateral.csv","text": "Depth: -9,7 mm  Channel: Lateral"}
}
]'

curl -v -k -H Content-Type:application/json -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects' --data '{ 
"title": "Wolf Krzysztof 2019-04-24",
"label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"false\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>",
"sampling": "Sequential sampling"
}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects/4/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-0,5_kanalCentral.csv","text": "Depth: -0,5 mm  Channel: Central"}
},
{
"id": 2,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-0,5_kanalLateral.csv","text": "Depth: -0,5 mm  Channel: Lateral"}
},
{
"id": 3,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-1,0_kanalCentral.csv","text": "Depth: -1,0 mm  Channel: Central"}
},
{
"id": 4,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-1,0_kanalLateral.csv","text": "Depth: -1,0 mm  Channel: Lateral"}
},
{
"id": 5,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-1,5_kanalCentral.csv","text": "Depth: -1,5 mm  Channel: Central"}
},
{
"id": 6,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-1,5_kanalLateral.csv","text": "Depth: -1,5 mm  Channel: Lateral"}
},
{
"id": 7,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-10,0_kanalCentral.csv","text": "Depth: -10,0 mm  Channel: Central"}
},
{
"id": 8,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-10,0_kanalLateral.csv","text": "Depth: -10,0 mm  Channel: Lateral"}
},
{
"id": 9,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-2,0_kanalCentral.csv","text": "Depth: -2,0 mm  Channel: Central"}
},
{
"id": 10,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-2,0_kanalLateral.csv","text": "Depth: -2,0 mm  Channel: Lateral"}
},
{
"id": 11,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-2,5_kanalCentral.csv","text": "Depth: -2,5 mm  Channel: Central"}
},
{
"id": 12,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-2,5_kanalLateral.csv","text": "Depth: -2,5 mm  Channel: Lateral"}
},
{
"id": 13,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-3,0_kanalCentral.csv","text": "Depth: -3,0 mm  Channel: Central"}
},
{
"id": 14,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-3,0_kanalLateral.csv","text": "Depth: -3,0 mm  Channel: Lateral"}
},
{
"id": 15,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-3,5_kanalCentral.csv","text": "Depth: -3,5 mm  Channel: Central"}
},
{
"id": 16,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-3,5_kanalLateral.csv","text": "Depth: -3,5 mm  Channel: Lateral"}
},
{
"id": 17,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-4,0_kanalCentral.csv","text": "Depth: -4,0 mm  Channel: Central"}
},
{
"id": 18,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-4,0_kanalLateral.csv","text": "Depth: -4,0 mm  Channel: Lateral"}
},
{
"id": 19,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-4,5_kanalCentral.csv","text": "Depth: -4,5 mm  Channel: Central"}
},
{
"id": 20,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-4,5_kanalLateral.csv","text": "Depth: -4,5 mm  Channel: Lateral"}
},
{
"id": 21,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-5,0_kanalCentral.csv","text": "Depth: -5,0 mm  Channel: Central"}
},
{
"id": 22,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-5,0_kanalLateral.csv","text": "Depth: -5,0 mm  Channel: Lateral"}
},
{
"id": 23,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-5,5_kanalCentral.csv","text": "Depth: -5,5 mm  Channel: Central"}
},
{
"id": 24,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-5,5_kanalLateral.csv","text": "Depth: -5,5 mm  Channel: Lateral"}
},
{
"id": 25,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-6,0_kanalCentral.csv","text": "Depth: -6,0 mm  Channel: Central"}
},
{
"id": 26,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-6,0_kanalLateral.csv","text": "Depth: -6,0 mm  Channel: Lateral"}
},
{
"id": 27,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-7,0_kanalCentral.csv","text": "Depth: -7,0 mm  Channel: Central"}
},
{
"id": 28,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-7,0_kanalLateral.csv","text": "Depth: -7,0 mm  Channel: Lateral"}
},
{
"id": 29,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-8,0_kanalCentral.csv","text": "Depth: -8,0 mm  Channel: Central"}
},
{
"id": 30,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-8,0_kanalLateral.csv","text": "Depth: -8,0 mm  Channel: Lateral"}
},
{
"id": 31,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-8,5_kanalCentral.csv","text": "Depth: -8,5 mm  Channel: Central"}
},
{
"id": 32,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-8,5_kanalLateral.csv","text": "Depth: -8,5 mm  Channel: Lateral"}
},
{
"id": 33,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-9,0_kanalCentral.csv","text": "Depth: -9,0 mm  Channel: Central"}
},
{
"id": 34,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-9,0_kanalLateral.csv","text": "Depth: -9,0 mm  Channel: Lateral"}
},
{
"id": 35,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-9,5_kanalCentral.csv","text": "Depth: -9,5 mm  Channel: Central"}
},
{
"id": 36,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth-9,5_kanalLateral.csv","text": "Depth: -9,5 mm  Channel: Lateral"}
},
{
"id": 37,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth0,0_kanalCentral.csv","text": "Depth: 0,0 mm  Channel: Central"}
},
{
"id": 38,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth0,0_kanalLateral.csv","text": "Depth: 0,0 mm  Channel: Lateral"}
},
{
"id": 39,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth0,5_kanalCentral.csv","text": "Depth: 0,5 mm  Channel: Central"}
},
{
"id": 40,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth0,5_kanalLateral.csv","text": "Depth: 0,5 mm  Channel: Lateral"}
},
{
"id": 41,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth1,0_kanalCentral.csv","text": "Depth: 1,0 mm  Channel: Central"}
},
{
"id": 42,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth1,0_kanalLateral.csv","text": "Depth: 1,0 mm  Channel: Lateral"}
},
{
"id": 43,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth1,5_kanalCentral.csv","text": "Depth: 1,5 mm  Channel: Central"}
},
{
"id": 44,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth1,5_kanalLateral.csv","text": "Depth: 1,5 mm  Channel: Lateral"}
},
{
"id": 45,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth2,0_kanalCentral.csv","text": "Depth: 2,0 mm  Channel: Central"}
},
{
"id": 46,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth2,0_kanalLateral.csv","text": "Depth: 2,0 mm  Channel: Lateral"}
},
{
"id": 47,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth2,5_kanalCentral.csv","text": "Depth: 2,5 mm  Channel: Central"}
},
{
"id": 48,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth2,5_kanalLateral.csv","text": "Depth: 2,5 mm  Channel: Lateral"}
},
{
"id": 49,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth3,0_kanalCentral.csv","text": "Depth: 3,0 mm  Channel: Central"}
},
{
"id": 50,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth3,0_kanalLateral.csv","text": "Depth: 3,0 mm  Channel: Lateral"}
},
{
"id": 51,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth3,5_kanalCentral.csv","text": "Depth: 3,5 mm  Channel: Central"}
},
{
"id": 52,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546253247/depth3,5_kanalLateral.csv","text": "Depth: 3,5 mm  Channel: Lateral"}
}
]'

curl -v -k -H Content-Type:application/json -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects' --data '{ 
"title": "Wolf Krzysztof 2019-04-24",
"label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"false\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>",
"sampling": "Sequential sampling"
}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects/5/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-0,5_kanalCentral.csv","text": "Depth: -0,5 mm  Channel: Central"}
},
{
"id": 2,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-0,5_kanalLateral.csv","text": "Depth: -0,5 mm  Channel: Lateral"}
},
{
"id": 3,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-1,0_kanalCentral.csv","text": "Depth: -1,0 mm  Channel: Central"}
},
{
"id": 4,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-1,0_kanalLateral.csv","text": "Depth: -1,0 mm  Channel: Lateral"}
},
{
"id": 5,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-1,5_kanalCentral.csv","text": "Depth: -1,5 mm  Channel: Central"}
},
{
"id": 6,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-1,5_kanalLateral.csv","text": "Depth: -1,5 mm  Channel: Lateral"}
},
{
"id": 7,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-10,0_kanalCentral.csv","text": "Depth: -10,0 mm  Channel: Central"}
},
{
"id": 8,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-10,0_kanalLateral.csv","text": "Depth: -10,0 mm  Channel: Lateral"}
},
{
"id": 9,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-2,0_kanalCentral.csv","text": "Depth: -2,0 mm  Channel: Central"}
},
{
"id": 10,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-2,0_kanalLateral.csv","text": "Depth: -2,0 mm  Channel: Lateral"}
},
{
"id": 11,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-2,5_kanalCentral.csv","text": "Depth: -2,5 mm  Channel: Central"}
},
{
"id": 12,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-2,5_kanalLateral.csv","text": "Depth: -2,5 mm  Channel: Lateral"}
},
{
"id": 13,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-3,0_kanalCentral.csv","text": "Depth: -3,0 mm  Channel: Central"}
},
{
"id": 14,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-3,0_kanalLateral.csv","text": "Depth: -3,0 mm  Channel: Lateral"}
},
{
"id": 15,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-3,5_kanalCentral.csv","text": "Depth: -3,5 mm  Channel: Central"}
},
{
"id": 16,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-3,5_kanalLateral.csv","text": "Depth: -3,5 mm  Channel: Lateral"}
},
{
"id": 17,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-4,0_kanalCentral.csv","text": "Depth: -4,0 mm  Channel: Central"}
},
{
"id": 18,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-4,0_kanalLateral.csv","text": "Depth: -4,0 mm  Channel: Lateral"}
},
{
"id": 19,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-4,5_kanalCentral.csv","text": "Depth: -4,5 mm  Channel: Central"}
},
{
"id": 20,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-4,5_kanalLateral.csv","text": "Depth: -4,5 mm  Channel: Lateral"}
},
{
"id": 21,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-5,0_kanalCentral.csv","text": "Depth: -5,0 mm  Channel: Central"}
},
{
"id": 22,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-5,0_kanalLateral.csv","text": "Depth: -5,0 mm  Channel: Lateral"}
},
{
"id": 23,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-5,5_kanalCentral.csv","text": "Depth: -5,5 mm  Channel: Central"}
},
{
"id": 24,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-5,5_kanalLateral.csv","text": "Depth: -5,5 mm  Channel: Lateral"}
},
{
"id": 25,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-6,0_kanalCentral.csv","text": "Depth: -6,0 mm  Channel: Central"}
},
{
"id": 26,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-6,0_kanalLateral.csv","text": "Depth: -6,0 mm  Channel: Lateral"}
},
{
"id": 27,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-7,0_kanalCentral.csv","text": "Depth: -7,0 mm  Channel: Central"}
},
{
"id": 28,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-7,0_kanalLateral.csv","text": "Depth: -7,0 mm  Channel: Lateral"}
},
{
"id": 29,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-8,0_kanalCentral.csv","text": "Depth: -8,0 mm  Channel: Central"}
},
{
"id": 30,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-8,0_kanalLateral.csv","text": "Depth: -8,0 mm  Channel: Lateral"}
},
{
"id": 31,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-9,0_kanalCentral.csv","text": "Depth: -9,0 mm  Channel: Central"}
},
{
"id": 32,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth-9,0_kanalLateral.csv","text": "Depth: -9,0 mm  Channel: Lateral"}
},
{
"id": 33,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth0,0_kanalCentral.csv","text": "Depth: 0,0 mm  Channel: Central"}
},
{
"id": 34,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth0,0_kanalLateral.csv","text": "Depth: 0,0 mm  Channel: Lateral"}
},
{
"id": 35,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth0,5_kanalCentral.csv","text": "Depth: 0,5 mm  Channel: Central"}
},
{
"id": 36,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth0,5_kanalLateral.csv","text": "Depth: 0,5 mm  Channel: Lateral"}
},
{
"id": 37,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth1,0_kanalCentral.csv","text": "Depth: 1,0 mm  Channel: Central"}
},
{
"id": 38,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth1,0_kanalLateral.csv","text": "Depth: 1,0 mm  Channel: Lateral"}
},
{
"id": 39,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth1,5_kanalCentral.csv","text": "Depth: 1,5 mm  Channel: Central"}
},
{
"id": 40,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth1,5_kanalLateral.csv","text": "Depth: 1,5 mm  Channel: Lateral"}
},
{
"id": 41,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth2,0_kanalCentral.csv","text": "Depth: 2,0 mm  Channel: Central"}
},
{
"id": 42,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth2,0_kanalLateral.csv","text": "Depth: 2,0 mm  Channel: Lateral"}
},
{
"id": 43,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth2,5_kanalCentral.csv","text": "Depth: 2,5 mm  Channel: Central"}
},
{
"id": 44,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546257001/depth2,5_kanalLateral.csv","text": "Depth: 2,5 mm  Channel: Lateral"}
}
]'

curl -v -k -H Content-Type:application/json -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects' --data '{ 
"title": "Wolf Krzysztof 2019-04-24",
"label_config": "<View> <Header size=\"4\" underline=\"true\" value=\"$name\" /> <TimeSeries name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" overviewWidth=\"1%\" timeColumn=\"Time\"> <Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\" fixedScale=\"false\" /> <Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\" fixedScale=\"false\" /> </TimeSeries> <TimeSeriesLabels name=\"label\" toName=\"ts\"> <Label value=\"Skorupa lub prazkowie\" background=\"#80ff00\" /> <Label value=\"Czesci zewnetrzne galki bladej (5-6 mm przed celem)\" background=\"#D4380D\" /> <Label value=\"Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)\" background=\"#FFC069\" /> </TimeSeriesLabels> </View>",
"sampling": "Sequential sampling"
}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token b0a04e88161975f85c20959eabfe373f26f8b2bd' -X POST 'http://localhost/dbs/labels//api/projects/6/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-0,5_kanalAnterior.csv","text": "Depth: -0,5 mm  Channel: Anterior"}
},
{
"id": 2,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-0,5_kanalCentral.csv","text": "Depth: -0,5 mm  Channel: Central"}
},
{
"id": 3,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-1,0_kanalAnterior.csv","text": "Depth: -1,0 mm  Channel: Anterior"}
},
{
"id": 4,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-1,0_kanalCentral.csv","text": "Depth: -1,0 mm  Channel: Central"}
},
{
"id": 5,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-1,5_kanalAnterior.csv","text": "Depth: -1,5 mm  Channel: Anterior"}
},
{
"id": 6,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-1,5_kanalCentral.csv","text": "Depth: -1,5 mm  Channel: Central"}
},
{
"id": 7,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-10,0_kanalAnterior.csv","text": "Depth: -10,0 mm  Channel: Anterior"}
},
{
"id": 8,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-10,0_kanalCentral.csv","text": "Depth: -10,0 mm  Channel: Central"}
},
{
"id": 9,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-2,0_kanalAnterior.csv","text": "Depth: -2,0 mm  Channel: Anterior"}
},
{
"id": 10,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-2,0_kanalCentral.csv","text": "Depth: -2,0 mm  Channel: Central"}
},
{
"id": 11,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-2,5_kanalAnterior.csv","text": "Depth: -2,5 mm  Channel: Anterior"}
},
{
"id": 12,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-2,5_kanalCentral.csv","text": "Depth: -2,5 mm  Channel: Central"}
},
{
"id": 13,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-3,0_kanalAnterior.csv","text": "Depth: -3,0 mm  Channel: Anterior"}
},
{
"id": 14,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-3,0_kanalCentral.csv","text": "Depth: -3,0 mm  Channel: Central"}
},
{
"id": 15,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-3,5_kanalAnterior.csv","text": "Depth: -3,5 mm  Channel: Anterior"}
},
{
"id": 16,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-3,5_kanalCentral.csv","text": "Depth: -3,5 mm  Channel: Central"}
},
{
"id": 17,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-4,0_kanalAnterior.csv","text": "Depth: -4,0 mm  Channel: Anterior"}
},
{
"id": 18,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-4,0_kanalCentral.csv","text": "Depth: -4,0 mm  Channel: Central"}
},
{
"id": 19,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-4,5_kanalAnterior.csv","text": "Depth: -4,5 mm  Channel: Anterior"}
},
{
"id": 20,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-4,5_kanalCentral.csv","text": "Depth: -4,5 mm  Channel: Central"}
},
{
"id": 21,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-5,0_kanalAnterior.csv","text": "Depth: -5,0 mm  Channel: Anterior"}
},
{
"id": 22,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-5,0_kanalCentral.csv","text": "Depth: -5,0 mm  Channel: Central"}
},
{
"id": 23,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-6,0_kanalAnterior.csv","text": "Depth: -6,0 mm  Channel: Anterior"}
},
{
"id": 24,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-6,0_kanalCentral.csv","text": "Depth: -6,0 mm  Channel: Central"}
},
{
"id": 25,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-7,0_kanalAnterior.csv","text": "Depth: -7,0 mm  Channel: Anterior"}
},
{
"id": 26,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-7,0_kanalCentral.csv","text": "Depth: -7,0 mm  Channel: Central"}
},
{
"id": 27,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-8,0_kanalAnterior.csv","text": "Depth: -8,0 mm  Channel: Anterior"}
},
{
"id": 28,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-8,0_kanalCentral.csv","text": "Depth: -8,0 mm  Channel: Central"}
},
{
"id": 29,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-9,0_kanalAnterior.csv","text": "Depth: -9,0 mm  Channel: Anterior"}
},
{
"id": 30,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth-9,0_kanalCentral.csv","text": "Depth: -9,0 mm  Channel: Central"}
},
{
"id": 31,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth0,0_kanalAnterior.csv","text": "Depth: 0,0 mm  Channel: Anterior"}
},
{
"id": 32,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth0,0_kanalCentral.csv","text": "Depth: 0,0 mm  Channel: Central"}
},
{
"id": 33,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth0,5_kanalAnterior.csv","text": "Depth: 0,5 mm  Channel: Anterior"}
},
{
"id": 34,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth0,5_kanalCentral.csv","text": "Depth: 0,5 mm  Channel: Central"}
},
{
"id": 35,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth1,0_kanalAnterior.csv","text": "Depth: 1,0 mm  Channel: Anterior"}
},
{
"id": 36,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth1,0_kanalCentral.csv","text": "Depth: 1,0 mm  Channel: Central"}
},
{
"id": 37,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth1,5_kanalAnterior.csv","text": "Depth: 1,5 mm  Channel: Anterior"}
},
{
"id": 38,
"data": {"csv": "http://localhost/dbs/static//Wolf Krzysztof/546258766/depth1,5_kanalCentral.csv","text": "Depth: 1,5 mm  Channel: Central"}
}
]'


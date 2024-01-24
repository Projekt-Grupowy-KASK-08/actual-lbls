curl -v -k -H Content-Type:application/json -H 'Authorization: Token d80982a6a7b9d55a113e4c0f5bf15c84b32aea6e' -X POST 'http://localhost:8080/api/projects' --data '{ 
"title": "530614040",
"label_config": "<View><Header size=\"4\" underline=\"true\" value=\"$name\"></Header><TimeSeries fixedScale=\"true\" name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" timeColumn=\"Time\"><Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\"/><Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\"/></TimeSeries><Choices name=\"choices\" toName=\"ts\" required=\"true\"><Choice value=\"Skorupa lub prążkowie\"/><Choice value=\"Części zewnętrzne gałki bladej (5-6 mm przed celem)\"/><Choice value=\"Części wewnętrzne gałki bladej (2-3 mm przed celem do 1 mm za celem)\"/></Choices><!-- No region selected section --><View visibleWhen=\"no-region-selected\"><TimeSeriesLabels name=\"label\" toName=\"ts\"><Label value=\"Region\" background=\"#5b5\"/></TimeSeriesLabels></View></View>",
"sampling": "Sequential sampling"

}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token d80982a6a7b9d55a113e4c0f5bf15c84b32aea6e' -X POST 'http://localhost:8080/api/projects/1/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-10,0_kanalCentral.csv"}
},
{
"id": 2,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-10,0_kanalLateral.csv"}
},
{
"id": 3,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-4,3_kanalCentral.csv"}
},
{
"id": 4,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-4,3_kanalLateral.csv"}
},
{
"id": 5,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-4,6_kanalCentral.csv"}
},
{
"id": 6,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-4,6_kanalLateral.csv"}
},
{
"id": 7,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-4,9_kanalCentral.csv"}
},
{
"id": 8,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-4,9_kanalLateral.csv"}
},
{
"id": 9,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-5,2_kanalCentral.csv"}
},
{
"id": 10,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-5,2_kanalLateral.csv"}
},
{
"id": 11,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-5,5_kanalCentral.csv"}
},
{
"id": 12,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-5,5_kanalLateral.csv"}
},
{
"id": 13,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-5,8_kanalCentral.csv"}
},
{
"id": 14,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-5,8_kanalLateral.csv"}
},
{
"id": 15,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-6,1_kanalCentral.csv"}
},
{
"id": 16,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-6,1_kanalLateral.csv"}
},
{
"id": 17,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-6,4_kanalCentral.csv"}
},
{
"id": 18,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-6,4_kanalLateral.csv"}
},
{
"id": 19,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-6,7_kanalCentral.csv"}
},
{
"id": 20,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-6,7_kanalLateral.csv"}
},
{
"id": 21,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,0_kanalCentral.csv"}
},
{
"id": 22,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,0_kanalLateral.csv"}
},
{
"id": 23,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,3_kanalCentral.csv"}
},
{
"id": 24,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,3_kanalLateral.csv"}
},
{
"id": 25,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,6_kanalCentral.csv"}
},
{
"id": 26,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,6_kanalLateral.csv"}
},
{
"id": 27,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,9_kanalCentral.csv"}
},
{
"id": 28,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-7,9_kanalLateral.csv"}
},
{
"id": 29,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-8,2_kanalCentral.csv"}
},
{
"id": 30,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-8,2_kanalLateral.csv"}
},
{
"id": 31,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-8,5_kanalCentral.csv"}
},
{
"id": 32,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-8,5_kanalLateral.csv"}
},
{
"id": 33,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-8,8_kanalCentral.csv"}
},
{
"id": 34,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-8,8_kanalLateral.csv"}
},
{
"id": 35,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-9,1_kanalCentral.csv"}
},
{
"id": 36,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-9,1_kanalLateral.csv"}
},
{
"id": 37,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-9,4_kanalCentral.csv"}
},
{
"id": 38,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-9,4_kanalLateral.csv"}
},
{
"id": 39,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-9,7_kanalCentral.csv"}
},
{
"id": 40,
"data": {"csv": "http://localhost:8787/AT/530614040/depth-9,7_kanalLateral.csv"}
}
]'

curl -v -k -H Content-Type:application/json -H 'Authorization: Token d80982a6a7b9d55a113e4c0f5bf15c84b32aea6e' -X POST 'http://localhost:8080/api/projects' --data '{ 
"title": "530619803",
"label_config": "<View><Header size=\"4\" underline=\"true\" value=\"$name\"></Header><TimeSeries fixedScale=\"true\" name=\"ts\" valueType=\"url\" value=\"$csv\" sep=\",\" timeColumn=\"Time\"><Channel column=\"1: Raw\" strokeColor=\"#17b\" legend=\"Raw\" units=\"Activity\"/><Channel column=\"2: Preprocessed\" strokeColor=\"#f70\" legend=\"Preprocessed\" units=\"Activity\"/></TimeSeries><Choices name=\"choices\" toName=\"ts\" required=\"true\"><Choice value=\"Skorupa lub prążkowie\"/><Choice value=\"Części zewnętrzne gałki bladej (5-6 mm przed celem)\"/><Choice value=\"Części wewnętrzne gałki bladej (2-3 mm przed celem do 1 mm za celem)\"/></Choices><!-- No region selected section --><View visibleWhen=\"no-region-selected\"><TimeSeriesLabels name=\"label\" toName=\"ts\"><Label value=\"Region\" background=\"#5b5\"/></TimeSeriesLabels></View></View>",
"sampling": "Sequential sampling"

}'

curl -H 'Content-Type: application/json' -H 'Authorization: Token d80982a6a7b9d55a113e4c0f5bf15c84b32aea6e' -X POST 'http://localhost:8080/api/projects/2/import' -d '[
{
"id": 1,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-10,0_kanalCentral.csv"}
},
{
"id": 2,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-10,0_kanalLateral.csv"}
},
{
"id": 3,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-7,3_kanalCentral.csv"}
},
{
"id": 4,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-7,6_kanalCentral.csv"}
},
{
"id": 5,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-7,6_kanalLateral.csv"}
},
{
"id": 6,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-7,9_kanalCentral.csv"}
},
{
"id": 7,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-7,9_kanalLateral.csv"}
},
{
"id": 8,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-8,2_kanalCentral.csv"}
},
{
"id": 9,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-8,2_kanalLateral.csv"}
},
{
"id": 10,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-8,5_kanalCentral.csv"}
},
{
"id": 11,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-8,5_kanalLateral.csv"}
},
{
"id": 12,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-8,8_kanalCentral.csv"}
},
{
"id": 13,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-8,8_kanalLateral.csv"}
},
{
"id": 14,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-9,1_kanalCentral.csv"}
},
{
"id": 15,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-9,1_kanalLateral.csv"}
},
{
"id": 16,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-9,4_kanalCentral.csv"}
},
{
"id": 17,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-9,4_kanalLateral.csv"}
},
{
"id": 18,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-9,7_kanalCentral.csv"}
},
{
"id": 19,
"data": {"csv": "http://localhost:8787/AT/530619803/depth-9,7_kanalLateral.csv"}
}
]'


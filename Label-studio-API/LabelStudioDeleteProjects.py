LABEL_STUDIO_URL = 'http://localhost/dbs/labels/'
FIRST_PROJECT_ID = 38
LAST_PROJECT_ID = 45
OUTPUT_DIR = r"C:\semestr 6\actual-lbls\Label-studio-API"  # path to save the script
TOKEN = "bf7e7d843681e97e6a0bc32535cb26a69fbae376"


#curl -X DELETE http://localhost:8080/api/projects/{id} -H 'Authorization: Token twojTokenAPI'

f_p = open(OUTPUT_DIR + "/DeleteProjects.sh", "w")
for i in range(FIRST_PROJECT_ID, LAST_PROJECT_ID+1):
    f_p.write("curl -X DELETE " + LABEL_STUDIO_URL + "/api/projects/" + str(i) + " -H 'Authorization: Token " + TOKEN + "'\n")
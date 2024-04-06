LABEL_STUDIO_URL = 'http://localhost:8080/'
FIRST_PROJECT_ID = 1
LAST_PROJECT_ID = 25
OUTPUT_DIR = r"C:\semestr 6\actual-lbls\parser"  # path to save the script
TOKEN = "c22f991b21835d86e7a9485c9629640340aaf692"


#curl -X DELETE http://localhost:8080/api/projects/{id} -H 'Authorization: Token twojTokenAPI'

f_p = open(OUTPUT_DIR + "/DeleteProjects.sh", "w")
for i in range(FIRST_PROJECT_ID, LAST_PROJECT_ID+1):
    f_p.write("curl -X DELETE " + LABEL_STUDIO_URL + "/api/projects/" + str(i) + " -H 'Authorization: Token " + TOKEN + "'\n")
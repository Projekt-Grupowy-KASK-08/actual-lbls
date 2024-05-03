LABEL_STUDIO_URL = 'https://kask.eti.pg.edu.pl/dbs/labels/'
FIRST_PROJECT_ID = 791
LAST_PROJECT_ID = 1025
OUTPUT_DIR = r"C:\semestr 6\actual-lbls\parser"  # path to save the script
TOKEN = ""


#curl -X DELETE http://localhost:8080/api/projects/{id} -H 'Authorization: Token twojTokenAPI'

f_p = open(OUTPUT_DIR + "/DeleteProjects.sh", "w")
for i in range(FIRST_PROJECT_ID, LAST_PROJECT_ID+1):
    f_p.write("curl -X DELETE " + LABEL_STUDIO_URL + "/api/projects/" + str(i) + " -H 'Authorization: Token " + TOKEN + "'\n")
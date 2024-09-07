from credentials import LABEL_STUDIO_URL, OUTPUT_DIR, TOKEN

FIRST_PROJECT_ID = 38
LAST_PROJECT_ID = 45

#curl -X DELETE http://localhost:8080/api/projects/{id} -H 'Authorization: Token twojTokenAPI'

f_p = open(OUTPUT_DIR + "/DeleteProjects.sh", "w")
for i in range(FIRST_PROJECT_ID, LAST_PROJECT_ID+1):
    f_p.write("curl -X DELETE " + LABEL_STUDIO_URL + "/api/projects/" + str(i) + " -H 'Authorization: Token " + TOKEN + "'\n")
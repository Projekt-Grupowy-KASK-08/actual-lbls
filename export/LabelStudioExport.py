LABEL_STUDIO_URL = 'http://localhost/dbs/labels'
FIRST_PROJECT_ID = 2
LAST_PROJECT_ID = 7
TOKEN = "bf7e7d843681e97e6a0bc32535cb26a69fbae376"

f = open("ExportTasks.sh", "w")
for i in range(FIRST_PROJECT_ID, LAST_PROJECT_ID + 1):
    f.write("curl -X GET \"")
    f.write(LABEL_STUDIO_URL + "/api/projects/" + str(i))
    f.write("/export\" -H \"Authorization: Token ")
    f.write(TOKEN)
    f.write("\" --output \"annotations"+str(i)+".csv\"")
    f.write("\n")

# importing required libraries
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="lgj19",
  passwd ="414ee7d2",
  database = "acb"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()

# create & execute query
query = "SELECT * FROM teamName WHERE id < 100"
cursorObject.execute(query)
 
# get result from query  
myresult = cursorObject.fetchall()
   
# print query
for x in myresult:
    print(x)
    
    
# disconnecting from server
dataBase.close()
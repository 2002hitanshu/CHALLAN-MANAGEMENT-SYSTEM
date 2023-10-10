
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="30092002")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE ENTERTHENAMEOFDATABASE") #ENTER THE NAME OF DATABASE
if mydb.is_connected():
    print("connected")
mydb.close()
mydb=mysql.connector.connect(host="localhost",user="root",passwd="30092002",database="ENTERTHENAMEOFDATABASE")#ENTER THE NAME OF DATABASE HERE ALSO
cursor = mydb.cursor()
sql ='''CREATE TABLE CHALLAN(
   VEHICLE_NAME VARCHAR(25) ,
   MANUFACTURER CHAR(25),
   MODEL VARCHAR(25),
   RC CHAR(10),
   REGESTRATION_NUMBER CHAR(10),
   CHALLAN_AMOUNT FLOAT,
   DAY_DATE_TIME VARCHAR(35),
   PLACE VARCHAR(20),
   REASON VARCHAR(25)
)'''
cursor.execute(sql)


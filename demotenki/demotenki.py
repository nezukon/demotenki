
import lnetatmo
import requests
import time
import json
import datetime
import pyodbc
from password import *

authorization = lnetatmo.ClientAuth(
    clientId = neta_id,
    clientSecret = neta_pw,
    username = email,
    password = std_pw,
    scope = ""
    )

devList = lnetatmo.WeatherStationData(authorization)

outdoors_temp = devList.lastData()['Outdoor']['Temperature']
outdoors_humi = devList.lastData()['Outdoor']['Humidity']

# print (time.time())
# print (time.time() * 1000)

posttime = time.time() * 1000
posttime = posttime + 32400000
posttime = str(posttime)
posttime = posttime[0:13]
posttime = '/Date(' + posttime + ")/"

datetime = datetime.datetime.now()
datetime = str(datetime)
datetime = datetime[0:19]
print(datetime)

outdoors_temp = str(outdoors_temp)
outdoors_humi = str(outdoors_humi)

# print(outdoors_temp)
# print(outdoors_humi)
# print(posttime)

head = {
        'Authorization':hdb_auth,
        'Content-Type':'application/json; charset=utf-8'
    }

obj = {
        'TIMESTAMP' : posttime,
        'TEMP' : outdoors_temp,
        'HUMI' : outdoors_humi
    }

json_data = json.dumps(obj).encode('utf-8')

print(json_data)

r = requests.post(
    'https://demoapps0018067025trial.hanatrial.ondemand.com/xs_demo/tenkidemo.xsodata/TENKI_DEMO',
    headers=head,
    data=json_data)

print(r)
print(r.text)


server = db_server
database = 'demo01'
username = db_uname
password = std_pw
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
sql = "INSERT INTO dbo.Tenki (TIMESTAMP, TEMP, HUMI) VALUES ('" + datetime + "','" + outdoors_temp + "','" + outdoors_humi + "')"
cursor.execute(sql)
cnxn.commit()



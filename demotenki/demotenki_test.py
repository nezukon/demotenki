import pyodbc

server = db_server
database = 'demo01'
username = db_uname
password = db_pword
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("INSERT INTO dbo.Tenki (TIMESTAMP, TEMP, HUMI) VALUES ('2018-01-14 19:20:00','10.0','50.0')")
cnxn.commit()







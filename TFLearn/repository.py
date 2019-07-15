import pyodbc 
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
server = config['database']['Server']
dbname = config['database']['Name']
user = config['database']['User']
psswd = config['database']['Psswd']

connectionString = 'Driver={SQL Server}' + ';Server={};Database={};Trusted_Connection=yes;UID={};PWD={};'.format(server, dbname, user, psswd)

conn = pyodbc.connect(connectionString)

def insert(user, emotion):
    now = datetime.datetime.now()
    date = now.strftime("%Y/%m/%d")
    time = now.strftime("%H:%M:%S")
    try:
        query = "INSERT INTO HappyTeam.dbo.SentimentByHour (Date, Time, Username, SentimentId) VALUES('{}', '{}', '{}', {})".format(date, time, user, emotion)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print(query)
    except:
        print('-------------------------------------')
#insert('Andrea Soria', 1)
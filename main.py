import pandas as pd
import os
from urllib.parse import quote
from sqlalchemy import create_engine,event, text

username = os.environ['RASP_MySQL_USER']
password = os.environ['RASP_MySQL_PASS']
ip = os.environ['RASP_MySQL_IP']
port = os.environ['RASP_MySQL_PORT']

eng = create_engine(f'mysql+pymysql://{username}:%s@{ip}:{port}' % quote(password))

@event.listens_for(eng,"connect",insert=True)
def connect(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()


conn = eng.connect()
conn.execute(text('USE GAXYLINA'))

q = 'SELECT * FROM ANIME'
data = pd.read_sql_query(text(q),conn)
print(data)

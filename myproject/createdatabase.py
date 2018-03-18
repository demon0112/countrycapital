import psycopg2
import csv

conn = psycopg2.connect(database = "testdb", user = "postgres", password = "demon0112", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE datag
    (
      COUNTRY   TEXT   ,
      CAPITAL    TEXT  
      );''')
print ("Table created successfully")
cur.execute('''COPY datag
FROM '/tmp/datac.csv' DELIMITER ',' CSV HEADER;''')
conn.commit()
conn.close()

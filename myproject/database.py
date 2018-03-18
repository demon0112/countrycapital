import psycopg2

conn = psycopg2.connect(database = "testdb", user = "postgres", password = "demon0112", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE cap
    (
      COUNTRY   TEXT   ,
      CAPITAL    TEXT  
      );''')
print ("Table created successfully")
cur.execute('''COPY cap(COUNTRY) 
FROM '/tmp/clist.csv' DELIMITER ','  CSV HEADER ;''')
cur.execute('''COPY cap(CAPITAL) 
FROM '/tmp/capitallist.csv' DELIMITER ','  CSV HEADER ;''')

conn.commit()
conn.close()


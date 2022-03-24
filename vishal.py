import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mulesoft")
mycursor.execute("CREATE DATABASE mulesoft")
mycursor.execute("USE mulesoft")
mycursor.execute("CREATE TABLE movies(name VARCHAR(255), "
                 "actor VARCHAR(255), "
                 "actress VARCHAR(255), "
                 "director VARCHAR(255), "
                 "year INT(4))")
sql = "INSERT INTO movies(name, actor, actress, director, year) VALUES (%s , %s, %s, %s, %s)"
val = [
('DANGAL', 'AMIR KHAN', 'SAKSHI TANWAR', 'NITESH TIWARI', 2012),
  ('TAARE ZAMEEN PAR', 'AAMIR KHAN', 'TISCA CHOPRA', 'AAMIR KHAN', 2007),
  ('SAAND KI AANKH', 'PRAKASH JHA', 'TAAPSEE PANNU', 'TUSAR HIRANANDANI', 2019),
  ('BHAAG MILKHA BHAAG', 'FARHAN AKHTAR', 'SONAM KAPOOR', 'RAKEYSH OMPRAKASH MEHRA', 2013),
  ('BHUJ', 'AJAY DEVGN', 'SONAKSHI SINHA', 'ABHISHEK DUDHAIYA', 2021),
  ('THE BIG BULL', 'ABHISHEK BACHCHAN', 'NIKITA DUTTA', 'KOOKIE GULATI',2021)
]
mycursor.executemany(sql, val)

mycursor.execute("SELECT * FROM movies")

result = mycursor.fetchall()

for row in result:
    print(row)

print("")
mycursor.execute("SELECT * FROM movies WHERE actor = 'AAMIR KHAN';")

result = mycursor.fetchall()

for row in result:
    print(row)

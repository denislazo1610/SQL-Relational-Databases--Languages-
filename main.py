import  sqlite3

conn = sqlite3.connect('Hablame.db')

c = conn.cursor()

c.execute('''CREATE TABLE people (Username text, Password text, Native_Language text, Learning_language text, minutes qty, Join_date text)''')

c.execute("INSERT INTO people VALUES ('Juan','tacosArethebest','Spanish','English', 30 , '2021-01-27')")
conn.commit()

c.execute("INSERT INTO people VALUES ('Josh','PeacetoTheworld','English', 'Spanish', 45 , '2021-01-30')")
conn.commit()

c.execute("INSERT INTO people VALUES ('Diana','DeathandLove','French', 'Spanish', 60 , '2021-01-30')")
conn.commit()

conn.close()
import  sqlite3


 
#In here, we are creating the database. 
name = input("Name your database file: ")
name = name + '.db'
print(name)


#In here, the new information will be 
#saved in the database that you created.
conn = sqlite3.connect(name)

# We must create a cursor. 
c = conn.cursor()

# We are creating a table in the database
c.execute('''CREATE TABLE users (Username text, Password text, Native_Language text, Learning_language text, minutes_of_use qty, Join_date text)''')


def addingvalues():
# We are adding new information to the table 
    c.execute("INSERT INTO users VALUES ('Juan','tacosArethebest','Spanish','English', 30 , '2021-01-27')")
    conn.commit()

c.execute("INSERT INTO users VALUES ('Josh','PeacetoTheworld','English', 'Spanish', 45 , '2021-01-30')")
conn.commit()

c.execute("INSERT INTO users VALUES ('Diana','DeathandLove','French', 'Spanish', 60 , '2021-01-30')")
conn.commit()

conn.close()
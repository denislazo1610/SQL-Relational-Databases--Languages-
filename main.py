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

def addingvalues(table, name, password, NL, LL, use, joinDate):
# We are adding new information to the table 
    sentence = "INSERT INTO "+ table + " VALUES (" + name + "," + password + "," + NL + "," + LL + "," + use + "," + joinDate + ")"
    c.execute(sentence)
    conn.commit()

def creatingTable(newTable): 
# We are creating a table in the database
    sentence = '''CREATE TABLE ''' + newTable + '''(Username text, Password text, Native_Language text, Learning_language text, minutes_of_use qty, Join_date text)'''
    c.execute(sentence)


def options():
    print("Choose a option:\n")
    print("\'A\' for adding a new table")
    print("\'B\' for adding a new entity to a table")

print("Hello, this is a Tracking programm! Which will keep the information of your users.")    
options()
choice = input('Enter your choice:')

c.execute("INSERT INTO users VALUES ('Josh','PeacetoTheworld','English', 'Spanish', 45 , '2021-01-30')")
conn.commit()

c.execute("INSERT INTO users VALUES ('Diana','DeathandLove','French', 'Spanish', 60 , '2021-01-30')")
conn.commit()

conn.close()
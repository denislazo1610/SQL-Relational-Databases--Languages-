import  sqlite3


 
#In here, we are creating the database. 
name = input("Name your database file: ")
name = name + '.db'
print(name)


#In here, the new information will be saved in the database that you created.
conn = sqlite3.connect(name)

# We must create a cursor. 
c = conn.cursor()

# We are creating a table in the database.
def creatingTable(newTable): 
    sentence = '''CREATE TABLE ''' + newTable + '''(Username text, Password text, Native_Language text, Learning_language text, minutes_of_use qty, Join_date text)'''
    c.execute(sentence)

# We are adding new information to the table. 
def addingvalues(table, name, password, NL, LL, use, joinDate):
    sentence = "INSERT INTO "+ table + " VALUES (" + name + "," + password + "," + NL + "," + LL + "," + use + "," + joinDate + ")"
    c.execute(sentence)
    conn.commit()

def options():
    print("Choose a option:\n")
    print("\'A\' for adding a new table")
    print("\'B\' for adding a new entity to a table")
    print("\'Exit\' for finish programm")


def action(choice, Tables):
    
    if ((choice == 'a') or (choice == 'A')):
        print('Creating a new table')
        options()
        choice = input('Enter your choice:')
        action()

    elif ((choice == 'b') or (choice == 'B')):
        print('Adding new Value to a table')
        options()
        choice = input('Enter your choice:')
        action()

    elif ((choice == 'exit') or (choice == 'Exit')):
        print('Thank you!')

print("Hello, this is a Tracking programm! Which will keep the information of your users.")    
options()
print('\n')
choice = input('Enter your choice:')
Tables = []
action(choice, Tables)

c.execute("INSERT INTO users VALUES ('Josh','PeacetoTheworld','English', 'Spanish', 45 , '2021-01-30')")
conn.commit()

c.execute("INSERT INTO users VALUES ('Diana','DeathandLove','French', 'Spanish', 60 , '2021-01-30')")
conn.commit()

conn.close()
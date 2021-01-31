import  sqlite3
import os
from user import values

 
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
    c.execute("INSERT INTO ? VALUES (?, ?, ?, ?, ? , ?)", (table, name, password, NL, LL, use, joinDate))
    conn.commit()

def options():
    print("Choose a option:\n")
    print("\'A\' for adding a new table")
    print("\'B\' for adding a new entity to a table")
    print("\'Exit\' for finish programm")


def action(choice, Tables):
    
    if ((choice == 'a') or (choice == 'A')):
        print('Creating a new table')
        newTable = input("what is your new table:")
        Tables.append(newTable)
        creatingTable(newTable)
        options()
        choice = input('Enter your choice:')
        action(choice, Tables)

    elif ((choice == 'b') or (choice == 'B')):
       
        print("This is all your tables: \n")
        for x in Tables:
            print(x)

        print('\n')
        selected = input('Which table you want to add: ')
        user = values.from_input()

        addingvalues(selected, user.username, user.password, user.NativeLanguage, user.LearningLanguage, user.minutes, user.joinDate)

        options()
        choice = input('Enter your choice:')
        action(choice, Tables)

    elif ((choice == 'exit') or (choice == 'Exit')):
        print('Thank you!')

print("Hello, this is a Tracking programm! Which will keep the information of your users.")    
options()
print('\n')
choice = input('Enter your choice:')
TablesNames = []
action(choice, TablesNames)

c.execute("INSERT INTO users VALUES ('Josh','PeacetoTheworld','English', 'Spanish', 45 , '2021-01-30')")
conn.commit()

c.execute("INSERT INTO users VALUES ('Diana','DeathandLove','French', 'Spanish', 60 , '2021-01-30')")
conn.commit()

conn.close()
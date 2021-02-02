import  sqlite3
import os
from user import values

print("Hello, this is a Tracking programm! Which will keep the information of your users.")   

#In here, we are creating the database. 
name = input("Name your database file: ")
name = name + '.db'
print(name)

os.system("cls")

#In here, the new information will be saved in the database that you created.
conn = sqlite3.connect(name)

# We must create a cursor. 
c = conn.cursor()

# We are creating a table in the database.

def creatingTable(newTable): 
    sentence ='CREATE TABLE IF NOT EXISTS ' + newTable + ' (Username text, Password text, Native_Language text, Learning_language text, minutes_of_use qty, Join_date text)'
    c.execute(sentence)
    conn.commit()

# We are adding new information to the table. 
def addingValues(table, name, password, NL, LL, use, joinDate):
    c.execute('''INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?)'''.format(table), (name, password, NL, LL, use, joinDate))
    conn.commit()

#You are modifying a value in a table
def modifyValue(table, placeNewValue, newValue, placeCondition, condition):
    c.execute('''UPDATE {} SET {} = (?) WHERE {} = (?)'''.format(table, placeNewValue, placeCondition), (newValue, condition))
    conn.commit()

#You are deleting a value from a table
def deletingValue(table, placeCondition, condition):
    c.execute('''DELETE FROM {} WHERE {} = (?)'''.format(table, placeCondition), ( condition, ))
    conn.commit()

def queryValue(table, placeCondition, condition):
    c.execute("SELECT * FROM {} WHERE {} = (?)".format(table, placeCondition), ( condition, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()

def options():
    print("Choose a option:\n")
    print("\'A\' for adding a new table")
    print("\'B\' for adding a new entity to a table")
    print("\'C\' for updating a value of a table")
    print("\'D\' for deleting a value of a table")
    print("\'E\' for query a value of a table")
    print("\'Exit\' for finish programm")


def action(choice, Tables):
    
    if ((choice == 'a') or (choice == 'A')):
        os.system("cls")
        print('Creating a new table\n')
        newTable = input("What is your new table:")
        Tables.append(newTable)
        creatingTable(newTable)

        os.system("cls")
        options()
        choice = input('Enter your choice:')
        action(choice, Tables) 

    elif ((choice == 'b') or (choice == 'B')):
        os.system("cls")
        print("This is all your tables: \n")
        for x in Tables:
            print(x)

        print('\n')
        selected = input('Which table you want to add: ')
        user = values.from_input()

        addingValues(selected, user.username, user.password, user.NativeLanguage, user.LearningLanguage, user.minutes, user.joinDate)

        os.system("cls")
        options()
        choice = input('Enter your choice:')
        action(choice, Tables)
    
    elif ((choice == 'c') or (choice == 'C')):
        os.system("cls")
        print('Updating')

        print("This is all your tables: \n")
        for x in Tables:
            print(x)
        print('\n')
        
        selected = input('Which table do you want to update? ')
        placeNewValue = input('What attributes do you want to change? ')
        newValue = input('What do you want to put in there instead? ')
        placeCondition = input('If there is a condition, in what attribute is your condition? ')
        condition = input('What is that condition? ')


        modifyValue(selected, placeNewValue, newValue, placeCondition, condition)

        os.system("cls")
        options()
        choice = input('Enter your choice:')
        action(choice, Tables)

    elif ((choice == 'd') or (choice == 'D')):
        os.system("cls")
        print("This is all your tables: \n")
        for x in Tables:
            print(x)
        print('\n')

        selected = input("From what table you want to delete? ")
        placeCondition = input("From what attribute? ")
        condition = input('With what  value? ')

        deletingValue(selected, placeCondition, condition)

        os.system("cls")
        options()
        choice = input('Enter your choice:')
        action(choice, Tables)

    elif ((choice == 'e') or (choice == 'E')):
        os.system("cls")
        print("query\n")
        selected = input('What table? ')
        placeCondition = input('From what attribute? ')
        condition = input("with what value? ")
        queryValue(selected, placeCondition, condition)

        os.system("cls")
        options()
        choice = input('Enter your choice:')
        action(choice, Tables)

    elif ((choice == 'exit') or (choice == 'Exit')):
        os.system("cls")
        print('Thank you!')



 
options()
print('\n')
choice = input('Enter your choice:')
TablesNames = []
action(choice, TablesNames)

conn.close()
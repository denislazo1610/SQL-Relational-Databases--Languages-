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

def options():
    print("Choose a option:\n")
    print("\'A\' for adding a new table")
    print("\'B\' for adding a new entity to a table")
    print("\'C\' for updating a value of a table")
    print("\'Exit\' for finish programm")


def action(choice, Tables):
    
    if ((choice == 'a') or (choice == 'A')):
        print('Creating a new table')
        newTable = input("What is your new table:")
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

        addingValues(selected, user.username, user.password, user.NativeLanguage, user.LearningLanguage, user.minutes, user.joinDate)

        options()
        choice = input('Enter your choice:')
        action(choice, Tables)
    
    elif ((choice == 'c') or (choice == 'C')):
        print('Updating')

        print("This is all your tables: \n")
        for x in Tables:
            print(x)
        
        selected = input('Which table do you want to update? ')
        placeNewValue = input('What attributes do you want to change? ')
        newValue = input('What do you want to put in there instead? ')
        placeCondition = input('If there is a condition, in what attribute is your condition? ')
        condition = input('What is that condition? ')


        modifyValue(selected, placeNewValue, newValue, placeCondition, condition)

    elif ((choice == 'exit') or (choice == 'Exit')):
        print('Thank you!')



print("Hello, this is a Tracking programm! Which will keep the information of your users.")    
options()
print('\n')
choice = input('Enter your choice:')
TablesNames = []
action(choice, TablesNames)

conn.close()
import  sqlite3

conn = sqlite3.connect('Example.db')

c = conn.cursor()

c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty, price real)''')

c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()

c.execute("INSERT INTO stocks VALUES ('2005-01-05','SELL','TON',450 ,25.6)")
conn.commit()

conn.close()
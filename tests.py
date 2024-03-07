import sqlite3

con = sqlite3.connect('users.db')
cursor = con.cursor()


cursor.execute("SELECT age, AVG(age) FROM users GROUP BY age")
res = cursor.fetchall()
for row in res:
  print(row)






con.commit()
con.close()
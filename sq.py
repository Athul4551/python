import sqlite3
conn=sqlite3.connect('table2.db')
cursor=conn.cursor()
# cursor.execute("create table STUDENT1(id text,name text,age text,city text)")
# data=[('1','anit','20','ettumanoor'),('2','athul','20','cherthala'),('3','jiya','22','ernakulam'),('4','sandra','21','ernakulam'),('5','ibru','22','ernakulam')]
# cursor.executemany("INSERT into STUDENT1(id,name,age,city)values(?,?,?,?)",data)
# conn.commit()
# conn.close()
# print("data inserted")

# p=cursor.execute("UPDATE STUDENT1 SET name = 'sandra' WHERE id=5")
# conn.commit()
# conn.close()
p=cursor.execute("DELETE FROM STUDENT1 WHERE name='edwin'")
conn.commit()
conn.close()
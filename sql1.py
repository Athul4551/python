import sqlite3
conn=sqlite3.connect('table.db')
cursor=conn.cursor()
# cursor.execute("create table STUDENT(rollno text,name text)")
# data=[('1','anit'),('2','athul'),('3','jiya'),('4','sandra')]
# cursor.executemany("insert into STUDENT(rollno,name)values(?,?)",data)
# p=cursor.execute("SELECT*FROM STUDENT")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()
# print("data inserted")

# p=cursor.execute("SELECT name FROM STUDENT")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()
# print("data inserted")

# p=cursor.execute("SELECT name FROM STUDENT WHERE rollno>2")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("UPDATE STUDENT SET name = 'ibru' WHERE rollno= 3 ")
# conn.commit()
# conn.close()

# p=cursor.execute("DELETE FROM STUDENT WHERE name='ibru'")
# conn.commit()
# conn.close()

# p=cursor.execute("SELECT MAX(rollno)FROM STUDENT")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()

# p=cursor.execute("SELECT name,COUNT(*)FROM STUDENT GROUP BY name")
# for i in p:
#     print(i)
# conn.commit()
# conn.close()
# print("data inserted")

# data=[('5','manu'),('6','maneesh'),('7','edwin'),('8','sandra')]
# cursor.executemany("insert into STUDENT(rollno,name)values(?,?)",data)
# conn.commit()
# conn.close()
# p=cursor.execute("DELETE FROM STUDENT WHERE name='maneesh'")
# conn.commit()
# conn.close()

p=cursor.execute("DROP TABLE STUDENT")
# conn.commit()
# conn.close()


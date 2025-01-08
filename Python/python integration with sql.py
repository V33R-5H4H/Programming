import mysql.connector as sql
connect=sql.connect(host='localhost',user="Veer",password="password",database="sem_3")
cur=connect.cursor()
cur.execute("select * from regions")
data=cur.fetchall()
print(data)
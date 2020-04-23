import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "",
    passwd = "",
    database = "pythonsql"
    )
mycursor = mydb.cursor()
data = [('harvey',19),('harey',17),('harlo',16)]
stmt = "Insert into `person`(`name`,`age`) values(%s,%s)"
#mycursor.execute("create table `person` (`id` integer(11) not null auto_increment,`name` varchar(225),age integer(11),primary key(id))")
#mycursor.executemany(stmt,data)
mycursor.execute("delete from `person` where `id` = 7 ")
mycursor.execute("select * from `person`")
myresult = mycursor.fetchall()


for i in myresult:
    print(i)
    
mydb.commit()
mycursor.close()
mydb.close()

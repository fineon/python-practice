import pymysql

# init empty html string
htmlString=""

# create an HTML <head>
def headhtml(htmlString):
  htmlString+="<!DOCTYPE html>\n<html lang='en>\n<head>\n<title>Owners of Pets</title>\n</head>\n<body>"
  return(htmlString)

# create a HTML footer
def foothtml(htmlString):
    htmlString+= "</body>\n</html>"
    return(htmlString)

# query the db
def ownerquery():
    print('start')
    db= pymysql.connect(host="localhost", user="root", db="slytherin")
    cursor= db.cursor()
    sql="SELECT * FROM owners;"
    cursor.execute(sql)
    owners= cursor.fetchall()
    sql = "SELECT column_name from information_schema.COLUMNS WHERE TABLE_NAME='owners';"
    cursor.execute(sql)

# first print python statements
# print('hello')
# print(12.4)

# booleanHere=True
# print(booleanHere)

# listHere=[1,2,3,4,5,6]
# print(listHere)

# this is a python comment. Connecting to mySQL localhost server
############

# server = pymysql.connect(host="localhost", user="root")
# cursor = server.cursor()

# sql  = "CREATE DATABASE IF NOT EXISTS slytherin;"
# cursor.execute(sql)

# sql = "USE slytherin;"
# cursor.execute(sql)

# sql= '''CREATE TABLE IF NOT EXISTS owners(
#     id integer NOT NULL AUTO_INCREMENT, 
#     name varchar(30) NOT NULL, 
#     gender varchar(7), 
#     phone varchar(10), 
#     PRIMARY KEY (id)  
#     );
# '''
# cursor.execute(sql)

# sql="SHOW tables"
# cursor.execute(sql)
# print(cursor.fetchall() )

# create another table in the above created db slytherin, called "pets"
# server = pymysql.connect(host="localhost", user="root", db="slytherin")
# cursor = server.cursor()

# sql = '''
# CREATE TABLE IF NOT EXISTS pets(
#     pet_id integer NOT NULL AUTO_INCREMENT, 
#     owner_id integer, 
#     name varchar(30), 
#     gender varchar(7), 
#     species varchar(20), 
#     color varchar(10), 
#     age integer, 
#     PRIMARY KEY (pet_id), 
#     FOREIGN KEY (owner_id) REFERENCES owners(id)
#     );'''
# cursor.execute(sql)

# sql="SHOW tables"
# cursor.execute(sql)
# print(cursor.fetchall() )

########### new SQL condition

# def load_owners(cursor):
#   owners_data = open("./owners.txt")
#   for rowline in owners_data:
#       row=rowline.split(",")
#       sql="INSERT INTO owners(name, gender, phone) VALUES('{}','{}','{}');".format(row[0],row[1],row[2])
#       cursor.execute(sql)
#       cursor.execute("SELECT * FROM owners;")
#       print(cursor.fetchall())

# def load_pets(cursor):
#   pets_data = open("./pets.txt")
#   for rowline in pets_data:
#       row=rowline.split(",")
#       sql="INSERT INTO pets(owner_id, name,gender,species,color,age) VALUES( (SELECT id FROM owners WHERE name='{0}'), '{1}','{2}','{3}','{4}','{5}');".format(*row)
#       cursor.execute(sql)
#       cursor.execute("SELECT * FROM pets;")
#       print(cursor.fetchall())

# if __name__ == "__main__":
#     db = pymysql.connect(host="localhost", user="root",db="slytherin")
#     cursor=db.cursor()
#     load_owners(cursor)
#     load_pets(cursor)
#     db.commit()
#     db.close()

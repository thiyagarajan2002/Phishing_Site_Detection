import mysql.connector
from Credentials import Credentials

cts=Credentials()
host_1,user_1,password_1=cts.host(),cts.user(),cts.password()

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=host_1,
            user=user_1,
            password=password_1
            )
        self.mycursor = self.mydb.cursor()

    def Create_database(self,db_name):
        sql="CREATE DATABASE "+db_name
        self.mycursor.execute(sql)

    def Delete_database(self,db_name):
        sql="Drop DATABASE "+db_name
        self.mycursor.execute(sql)

    def Show_database(self):
        sql="SHOW DATABASES"
        self.mycursor.execute(sql)
        ls=[]
        for x in self.mycursor.fetchall():
            ls.append(x)
        return ls
    
    def Exists_database(self,db_name):
        database_list=self.Show_database()
        for i in database_list:
            if i[0]==db_name:
                return True
            else:
                continue
        return False

#db=Database()
#db.Create_database("user_details")
#db.Delete_database("user_details")
#print(db.Show_database())
#print(db.Exists_database("user_details"))

class Table:
    def __init__(self,database_name):
        self.mydb = mysql.connector.connect(
        host=host_1,
        user=user_1,
        password=password_1,
        database=database_name
        )
        self.mycursor = self.mydb.cursor()

    def Create_table(self,table_name,columns):
        sql = f"CREATE TABLE {table_name} ({columns})"
        self.mycursor.execute(sql)
        self.mydb.commit()

    def Delete_table(self,table_name):
        sql = f"DROP TABLE IF EXISTS {table_name}"
        self.mycursor.execute(sql)
        self.mydb.commit()

    def Show_table(self):
        sql = "SHOW TABLES"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    def Exists_table(self,table_name):
        ls=self.Show_table()
        for i in ls:
            if table_name==i[0]:
                return True
            else:
                continue
        return False
    

#tb=Table("user_details")
#tb.Create_table("user_details","id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary FLOAT")
#tb.Delete_table("a")
"""
#Comment 1
    ls=[]
    for i in mycursor.fetchall():
        ls.append(i)
    return ls
"""
#print(tb.Show_table())
#print(tb.Exists_table("a"))

class Data:
    def __init__(self,database_name):
        self.mydb = mysql.connector.connect(
        host=host_1,
        user=user_1,
        password=password_1,
        database=database_name
        )
        self.mycursor = self.mydb.cursor()
    
    def Insert_data(self,table_name,data):
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.mycursor.execute(sql, tuple(data.values()))
        self.mydb.commit()

    def Read_data(self,table_name,columns,condition="true"):
        sql = f"SELECT {columns} FROM {table_name} where {condition}"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()

    def Update_data(self,table_name,column,condition='true'):
        sql=f"UPDATE {table_name} SET {column} WHERE {condition}"
        self.mycursor.execute(sql)
        self.mydb.commit()

    def Delete_data(self,table_name,condition):
        sql=f"DELETE FROM {table_name} WHERE {condition}"
        self.mycursor.execute(sql)
        self.mydb.commit()



#insert
#dt=Data("user_details")
#data = {"name": "John Smith","salary":30000}
#dt.Insert_data("user_details", data)

#read
#s=dt.Read_data('user_details','*','id=3')
#print(s)
#[(3, 'John Smith', 30000.0)]

#s=dt.Read_data('user_details','*')
#print(s)
#[(1, 'John Smith', 30000.0), (2, 'John Smith', 30000.0), (3, 'John Smith', 30000.0), (4, 'John Smith', 30000.0)]

#s=dt.Read_data('user_details','*',"id=3 AND salary=30000")
#print(s)
#[(3, 'John Smith', 30000.0)]


#update
#UPDATE table_name
#SET column1 = value1, column2 = value2, ...
#WHERE condition;
#dt.Update_data('user_details','name="trj"','id=1')

#delete
#dt.Delete_data('user_details','salary=30000 AND id=3')

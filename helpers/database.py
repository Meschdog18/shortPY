import mysql.connector

class Database():

    def __init__(self, host, user, password, db=None):
        self._host= host
        self._user= user
        self._password = password

        #create connection
        if db == None:
            self._create_con()
        else:
            self._create_con_with_db(db)
    def _create_con(self):
        mydb = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password
        )
        self._db = mydb
        #add error check
    def _create_con_with_db(self, db):
        mydb = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=db
        )
        self._db = mydb
        print(mydb)
    def create_database(self, name):
        mycursor = self._db.cursor()
        try:
            mycursor.execute("CREATE DATABASE {}".format(name))
            self._create_con_with_db(name)
        except Exception as ex:
            print(ex)
    def check_database_exist(self, name):
        databases = self._return_all_databases()
        for database in databases:
            if name==database[0]:
                return True
            else:
                return False
    def _return_all_databases(self):
        mycursor = self._db.cursor(buffered=True)
        mycursor.execute("SHOW DATABASES")

        return mycursor
    def create_table(self, name, columns):
        mycursor = self._db.cursor()
        try:
            mycursor.execute("CREATE TABLE {} ({})".format(name, columns))
        except Exception as ex:
            print(ex)
    def check_table_exist(self, name):
        tables = self._return_all_tables()
        for table in tables:
            if name==table[0]:
                return True
            else:
                return False
    def _return_all_tables(self):
        mycursor = self._db.cursor(buffered=True)
        mycursor.execute("SHOW TABLES")

        return mycursor
    def _parse_columns(self, columns):
        pass #todo so you dont have to write "(name VARCHAR(255))" for every column, instead have user give dict of {"columns":["column": {"name": "my col name", "size": 255}]}        
    def insert_into_table(self, name, columns, data):
        mycursor = self._db.cursor(buffered=True)
        mycursor.execute("INSERT INTO {} ({}) VALUES (%s, %s)".format(name, columns), (data[0], data[1]))
        #make it so you can add as many values as there is columns
        self._db.commit()
    def get_from_table(self, name , column ,short_id):
        mycursor = self._db.cursor(buffered=True)
        try:
            mycursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(name, column, short_id))

            value = mycursor.fetchone()
        except Exception as ex:
            print(ex)
        return value
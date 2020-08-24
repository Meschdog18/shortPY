from helpers.tools import Tools
from helpers.database import Database
from env_vars import Env_Vars

class Controller():
    #will control EVERYTHING
    def __init__(self):
        self._db = Database(Env_Vars["database"]["host"], Env_Vars["database"]["user"], Env_Vars["database"]["password"], "test")
        #db.create_database("test")
        #db.check_database_exist("test")
        coloumns = "id INT AUTO_INCREMENT PRIMARY KEY, mykey VARCHAR(255),long_url VARCHAR(255)"
        self._db.create_table("mytable", coloumns)
    def db_insert(self, url):
        mydb = self._db 
        try:
            key = self.prepare_url()
            mydb.insert_into_table("mytable", "mykey, long_url", [key, url])
            return key
        except Exception as ex:
            print(ex)
    def db_get(self, key):
        mydb = self._db
        try:
            return mydb.get_from_table("mytable", "mykey", key)[2]
        except Exception as ex:
            print(ex)
    def prepare_url(self):
        ID = Tools().genID()
        return ID
        
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
        self.db_insert("http://www.geeksengine.com/database/basic-select/column-alias.php")
        self.db_get("nwUMppd")
    def db_insert(self, url):
        mydb = self._db
        mydb.insert_into_table("mytable", "mykey, long_url", [self.prepare_url(), url])
    def db_get(self, key):
        mydb = self._db
        try:
            return mydb.get_from_table("mytable", "mykey", key)[2]
        except Exception as ex:
            print(ex)
    def prepare_url(self):
        ID = Tools().genID()
        return ID
        
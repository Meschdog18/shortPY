from helpers.tools import Tools
from helpers.database import Database
from env_vars import Env_Vars

class Controller():
    #will control EVERYTHING
    def __init__(self):
        db = Database(Env_Vars["database"]["host"], Env_Vars["database"]["user"], Env_Vars["database"]["password"], "test")
        db.create_database("test")
        db.check_database_exist("test")
        coloumns = "id INT AUTO_INCREMENT PRIMARY KEY, short_url VARCHAR(255),long_url VARCHAR(255)"
        db.create_table("mytable", coloumns)
        db.insert_into_table("mytable", "short_url, long_url", [self.prepare_url(), "https://www.w3schools.com/python/python_mysql_insert.asp"])
        print(db.get_from_table("mytable", "short_url", "mo3fObs")[2])
    def prepare_url(self):
        ID = Tools().genID()
        return ID
        
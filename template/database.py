import sqlite3
from sqlite3.dbapi2 import Cursor

class Database():
    def __init__(self,name = "system.db") -> None:
        self.name = name
        
    def conecta(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                     
                CREATE TABLE IF NOT EXISTS users(
                    
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    passoword TEXT NOT NULL,
                    access TEXT NOT NULL
                           );
                           
                           """)
        except AttributeError:
            print("Faça a Conexão com o Banco1")
            
    def insert_user(self,name,user,passaword,acess):
        try:
            cursor=self.connection.cursor()
            cursor.execute(""" 
                           
                INSERT INTO users(name,user,passaword,acess) VALUES (?,?,?,?)
            
                           """)(name,user,passaword,acess)
            self.connection.commit()
        except:
            print("Faça a conexão novaamente")
            
            


            
if __name__ =="__main__":
    
    db = Database()
    db.conecta()
    db.create_table_users()
    db.close_connection()
    
import sqlite3


class sqlite_db: 
    
    
    def __init__(self,banco = None): # Função cria banco de Dados
        self.conn = None
        self.cursor = None
        
        
        if banco:
            self.open(banco)
            
    
    def open(self,banco):
        
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão efetuada com sucesso!")
            
        except sqlite3.Error as e:
            print("Não foi estabelecida a conexão!")
            
            
            
    def criar_tabelas(self):
        
        cur = self.cursor
        cur.execute("""CREATE TABLE coletores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            serial TEXT UNIQUE NOT NULL,
            coletor TEXT UNIQUE NOT NULL,
            modelo TEXT NOT NULL,
            status TEXT NOT NULL
            )
            """)
        
        #TEXT UNIQUE NOT NULL
        #cargo TEXT NOT NULL,
            #acesso INTEGER
        
    def inserir_apaga_atualiza(self,query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()
        
    def pega_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()
        
    
            
#db = sqlite_db("sistema.db") # Nome do banco de Dados

#db.criar_tabelas() 
            
            
import sqlite3 as sql

class tableMainTitles():
    def __init__(self):

        self.create_table()
        
    def create_table(self):
        conn = sql.connect("lad.bd")
        cursor = conn.cursor()
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS maintitles (
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                titleJP VARCHAR(255) NOT NULL,
                                titleWE VARCHAR(255) NOT NULL,
                                yearJP VARCHAR(4) NOT NULL,
                                yearWE VARCHAR(4) NOT NULL,
                                platforms VARCHAR(255) NOT NULL
                            );
                            """)
        conn.commit()
        conn.close
        
    def newGame(self, nomeJP, nomeWE, anoJP, anoWE, platforms):
        conn = sql.connect("lad.bd")
        cursor = conn.cursor()
        cursor.execute(f"""
                            INSERT INTO maintitles(titleJP, titleWE, yearJP, yearWE, platforms)
                            VALUES('{nomeJP}', '{nomeWE}', '{anoJP}', '{anoWE}', '{platforms}');
                            """)
        conn.commit()
        conn.close()
    
    def listGames(self):
        conn = sql.connect("lad.bd")
        cursor = conn.cursor()
        titles = cursor.execute("SELECT * FROM maintitles")
        entries = []
        for item in titles.fetchall():
            entries.append({
             'id': item[0],
             'titleJP': item[1],
             'titleWE': item[2],
             'yearJP': item[3],
             'yearWE': item[4],
             'platforms': item[5],   
            })
        conn.close()
        return entries
    
    def updateGames(self, id, nomeJP, nomeWE, yearJP, yearWE, platform):
        conn = sql.connect("lad.bd")
        cursor = conn.cursor()
        cursor.execute(f"""
                            UPDATE maintitles
                            SET titleJP = '{nomeJP}',
                            titleWE = '{nomeWE}',
                            yearJP = '{yearJP}',
                            yearWE = '{yearWE}',
                            platforms = '{platform}'
                            WHERE id = {id}
                            """)
        conn.commit()
        conn.close()
        
    def deleteGame(self, id):
        conn = sql.connect("lad.bd")
        cursor = conn.cursor()
        cursor.execute(f"""
                            DELETE FROM maintitles
                            WHERE id={id}
                            """)
        conn.commit()
        conn.close
        
    def searchGame(self, id):
        conn = sql.connect("lad.bd")
        cursor = conn.cursor()
        title = cursor.execute(f"SELECT * FROM maintitles WHERE id={id}")
        item = title.fetchone()
        conn.close()
        return {
             'id': item[0],
             'titleJP': item[1],
             'titleWE': item[2],
             'yearJP': item[3],
             'yearWE': item[4],
             'platforms': item[5],   
            }
        

tblTitles = tableMainTitles()
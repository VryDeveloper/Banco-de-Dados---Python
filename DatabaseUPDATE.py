import sqlite3

banco = sqlite3.connect('Valorant.db')

cursor = banco.cursor()


cursor.execute("CREATE TABLE VALORANT_GUNS (Nome_Arma VARCHAR(20), Tipo_De_Arma VARCHAR(25))")
banco.commit()
banco.close
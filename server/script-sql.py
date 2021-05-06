import sqlite3

con = sqlite3.connect("../client/banco.db")#cria a base/banco de dados caso não exista.
cursor = con.cursor()#abrindo conexao

def initial():
	cursor.execute("CREATE TABLE centers("
		"indice INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
		"nome TEXT NOT NULL,"
		"nota_avaliacao REAL,"
		"localizacao TEXT NOT NULL,"
		"lista_coments TEXT);")
	print("Tabela criada")


def insert_default():
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Barão de Lucena', 5.0, 'Av. Caxangá, 3860 - Iputinga, Recife - PE, 50731-000', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Maria Lucinda', 5.0, 'Av. Parnamirim, 95 - Parnamirim, Recife - PE, 52060-000', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Usf Vila União', 5.0, 'R. Nova Aliança, s/n - Iputinga, Recife - PE, 50680-280', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA - Caxangá', 5.0, 'R. Ribeiro Pessoa, s/n - Iputinga, Recife - PE, 50980-000', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Nova Descoberta – Solano Trindade', 5.0, 'Av. Ver. Otacílio Azevedo, s/n - Nova Descoberta, Recife - PE, 52081-550', '');")
	con.commit()

initial()
insert_default()
con.close()
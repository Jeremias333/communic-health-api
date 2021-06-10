import sqlite3

con = sqlite3.connect("banco.db")#cria a base/banco de dados caso não exista.
cursor = con.cursor()#abrindo conexao

def initial():
	cursor.execute("CREATE TABLE centers("
		"indice INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
		"nome TEXT NOT NULL,"
		"nota_avaliacao REAL,"
		"localizacao TEXT NOT NULL,"
		"lista_coments TEXT);")
	print("Tabela de centers criada")
	cursor.execute("CREATE TABLE users("
		"indice INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
		"username VARCHAR,"
		"email VARCHAR,"
		"password VARCHAR,"
		"favorites VARCHAR);")
	print("Tabela de users criada")


def insert_default():
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Barão de Lucena', 5.0, 'Av. Caxangá, 3860 - Iputinga, Recife - PE, 50731-000', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Maria Lucinda', 5.0, 'Av. Parnamirim, 95 - Parnamirim, Recife - PE, 52060-000', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Usf Vila União', 5.0, 'R. Nova Aliança, s/n - Iputinga, Recife - PE, 50680-280', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA - Caxangá', 5.0, 'R. Ribeiro Pessoa, s/n - Iputinga, Recife - PE, 50980-000', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Nova Descoberta – Solano Trindade', 5.0, 'Av. Ver. Otacílio Azevedo, s/n - Nova Descoberta, Recife - PE, 52081-550', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital dos Servidores do Estado - HSE', 5.0, 'Av. Conselheiro Rosa e Silva, s/n - Espinheiro, Recife - PE, 52020-020', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Getúlio Vargas', 5.0, 'Av. Gen. San Martin, s/n - Cordeiro, Recife - PE, 50630-060', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Agamenon Magalhães', 5.0, 'Estr. do Arraial, 2723 - Casa Amarela, Recife - PE, 52070-230', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital da Restauração Gov. Paulo Guerra', 5.0, 'Av. Gov. Agamenon Magalhães, s/n - Derby, Recife - PE, 52171-011', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Curado - Unidade de Pronto Atendimento Médico Fernando de Lacerda', 5.0, 'R. Leonardo da Vinci, 68 - Curado II, Jaboatão dos Guararapes - PE, 54220-000', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Unidade de Pronto Atendimento Maria Esther Souto Carvalho', 5.0, 'Av. Mal. Mascarenhas de Morais, 4223 - Imbiribeira, Recife - PE, 51150-004', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA IBURA - Unidade de Pronto Atendimento Pediatra Zilda Arns', 5.0, 'R. Vale do Itajaí, S/n - Ibura, Recife - PE, 51280-405', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA - Unidade de Pronto Atendimento - Tipo III Torrões', 5.0, 'Av. Eng. Abdias de Carvalho, nº 30 - Torrões, Recife - PE, 50640-785', '');")
	cursor.execute("INSERT INTO users (username, email, password, favorites) VALUES ('jeremias333', 'jeremais@cummunichealth.com', '123456', '[1,2,3]');")
	con.commit()

initial()
insert_default()
con.close()
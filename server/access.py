import sqlite3

def get_all():
	obj = {
			"indices": [],
			"nomes": [],
			"nota_avaliacao": [],
			"localizacao": [],
			"lista_coments": []
		}
	
	with sqlite3.connect("banco.db") as con:
		cursor = con.cursor()
		cursor.execute("SELECT * FROM centers;")

		for linha in cursor.fetchall():
			obj["indices"].append(linha[0])
			obj["nomes"].append(linha[1])
			obj["nota_avaliacao"].append(linha[3])
			obj["localizacao"].append(linha[2])
			obj["lista_coments"].append(linha[4])

	return obj

def get_id_name():
	obj = {
			"indices": [],
			"nomes": [],
		}
	
	with sqlite3.connect("banco.db") as con:
		cursor = con.cursor()
		cursor.execute("SELECT indice,nome FROM centers;")

		for linha in cursor.fetchall():
			obj["indices"].append(linha[0])
			obj["nomes"].append(linha[1])

	return obj

def get_id_name_localization_rate(indice = 0):
	obj = {
			"indices": [],
			"nomes": [],
			"nota_avaliacao": [],
			"localizacao": []
		}
	
	with sqlite3.connect("banco.db") as con:
		cursor = con.cursor()
		cursor.execute(f"SELECT indice,nome,localizacao,nota_avaliacao FROM centers where indice == '{indice}';")

		for linha in cursor.fetchall():
			obj["indices"].append(linha[0])
			obj["nomes"].append(linha[1])
			obj["nota_avaliacao"].append(linha[3])
			obj["localizacao"].append(linha[2])

	return obj

def get_id_name_coments(indice = 0):
	obj = {
			"indices": [],
			"nomes": [],
			"lista_coments": []
		}
	
	with sqlite3.connect("banco.db") as con:
		cursor = con.cursor()
		cursor.execute(f"SELECT indice,nome,lista_coments FROM centers where indice == '{indice}';")

		for linha in cursor.fetchall():
			obj["indices"].append(linha[0])
			obj["nomes"].append(linha[1])
			obj["lista_coments"].append(linha[2])

	return obj

def add_comments(obj=None):
	obj_local = {
		"indice": obj["indice"],		
		"comentario": obj["lista_coments"]
	}

	indice = obj_local["indice"]
	comentario = obj_local["comentario"]

	with sqlite3.connect("banco.db") as con:
		cursor = con.cursor()

		cursor.execute(f"UPDATE centers SET lista_coments = '{comentario}' WHERE indice = '{indice}'")
		con.commit()
		msg = {"msg":"concluído"}

		return msg

def add_user(obj=None):
	obj_local = {
		"username": obj["username"],
		"email": obj["email"],
		"password": obj["password"]
	}

	username = obj_local["username"]
	email = obj_local["email"]
	password = obj_local["password"]

	if not exists_email_username(username, email):
		with sqlite3.connect("banco.db") as con:
			cursor = con.cursor()

			cursor.execute(f"INSERT INTO users (username, email, password) VALUES ('{username}','{email}','{password}');")
			con.commit()
			msg = {"msg":"signup concluído"}

			return msg
	else:
		msg = {"msg":"erro ao cadastrar"}
		return msg

def exists_email_username(username, email):
	db = list()

	with sqlite3.connect("banco.db") as con:
		cursor = con.cursor()

		cursor.execute(f"SELECT username, email FROM users;")
		
		for linha in cursor.fetchall():
			if linha[0] == username or linha[1] == email:
				print(linha[0], linha[1])
				return True
		return False

def do_login(obj=None):
	db_values = list()
	obj_local = {
		"username": obj["username"],
		"password": obj["password"]
	}

	username = obj_local["username"]
	password = obj_local["password"]

	with sqlite3.connect("banco.db") as con:
		cursor = con.cursor()

		cursor.execute(f"SELECT indice, username, password FROM users;")
		
		for linha in cursor.fetchall():
			db_values.append(linha[0])
			db_values.append(linha[1])
			db_values.append(linha[2])

	if username == db_values[1] and password == db_values[2]:
		obj_return = {
			"indice": db_values[0],
			"username": db_values[1],
			"password": db_values[2]
		}
		return obj_return
	else:
		msg = {"msg":"usuario ou senha inválidos"}
		return msg


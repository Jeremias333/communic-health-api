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
	return {"msg":"Error"}

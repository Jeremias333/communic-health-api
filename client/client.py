import os
import sqlite3
#request

con = sqlite3.connect("banco.db")#cria a base/banco de dados caso não exista.
cursor = con.cursor()#abrindo conexao

def start():
	clear()
	menu_principal = ("Bem vindos ao ComunicHealth, o que deseja fazer: \n\n"
			"1 - Lista de centros de saúde\n"
			"2 - Ajuda\n")

	print(menu_principal)
	opcao = int(input("Escolha uma opção (ex: 1): "))

	if opcao == 1:
		list_centers()

def list_centers():
	# pegariamos a lista de nomes e os indices de cada centro cadastrado

	lista = {
		"indice": [],
		"nome": []
	}

	cursor.execute("SELECT indice,nome FROM centers;")

	# print(type(cursor.fetchall))
	for linha in cursor.fetchall():
		lista["indice"].append(linha[0])
		lista["nome"].append(linha[1])

	menu_centers = "Escolha um centro médico cadastrado:\n\n"
	contador = 0
	escolhas = ""

	for indice in range(len(lista["indice"])):
		atual_indice = lista["indice"][indice]
		atual_nome = lista["nome"][indice]
		escolhas += f"{atual_indice} - {atual_nome}\n"
	escolhas += "\n0 - Sair"
	menu_centers += escolhas
	
	opcao = -1

	# print(lista["indice"][-1])

	while opcao < 0 or opcao > lista["indice"][-1]+1:
		clear()
		print(menu_centers)
		opcao = int(input("Escolha um centro de saúde (ex: 1): "))

		if opcao == 0:
			os.exit()
	info_center(opcao)

def info_center(indice):
	
	# aqui vai ficar o acesso a api e retornar os dados do hospital.
	# - Indice
	# - Nome 
	# - Nota de avaliação
	# - Lista de comentários

	lista = {
		"indice": 0,
		"nome": "",
		"localizacao": "",
		"nota_avaliacao": 0.0
	}

	cursor.execute(f"SELECT * FROM centers WHERE indice == {indice}")

	for linha in cursor.fetchall():
		lista["indice"] = linha[0]
		lista["nome"] = linha[1]
		lista["nota_avaliacao"] = linha[2]
		lista["localizacao"] = linha[3]

	print(lista)
	infos = "[INFORMAÇÕES]\n\n"+str(lista["indice"])+" - "+str(lista["nome"])
	infos += "\nLocalização: "+str(lista["localizacao"])
	infos += "\nAvaliação: "+str(lista["nota_avaliacao"])


	escolha = "\n1 - Ver comentários \n2 - Adicionar comentário \n3 - Voltar\n\n"

	opcao = -1

	while opcao < 0 or opcao > 3:
		clear()

		print(infos)

		print(escolha)

		opcao = int(input("Escolha uma ação (ex: 1): "))

		if opcao == 1:
			ver_coments(lista["indice"])
		if opcao == 2:
			adc_coments(lista["indice"])
		if opcao == 3:
			list_centers()

	
def adc_coments(indice):
	clear()
	# pesquisar nome do escolhido
	lista = {
		"indice": 0,
		"nome": "",
		"lista_coments" : ""
	}

	cursor.execute(f"SELECT * FROM centers WHERE indice == {indice}")

	for linha in cursor.fetchall():
		lista["indice"] = linha[0]
		lista["nome"] = linha[1]
		lista["lista_coments"] = linha[4]

	nome_indice = lista["nome"]
	separator = "$#&*$"

	menu = f"Você escolheu fazer um comentário sobre o centro de saúde: {nome_indice}"

	print(menu)

	comentario = input("\n\nDigite um comentário sobre (ex: Gostei muito do lugar, bem organizado...): ").strip()
	comentario += (lista["lista_coments"]+separator+comentario)

	cursor.execute(f"UPDATE centers SET lista_coments = '{comentario}' WHERE indice = '{indice}'")
	con.commit()

	clear()
	print("Comentário adicionado com sucesso: ")

	info_center(indice)

	# popular comentário

def ver_coments(indice):
	#baseado no indice carregar todos comentários do centro de saúde.
	lista = {
		"indice": 0,
		"nome": "",
		"lista_coments" : ""
	}

	

	cursor.execute(f"SELECT * FROM centers WHERE indice == {indice}")

	for linha in cursor.fetchall():
		lista["indice"] = linha[0]
		lista["nome"] = linha[1]
		lista["lista_coments"] = linha[4]

	comentarios = lista["lista_coments"].split("$#&*$")

	nome_indice = lista["nome"]
	separator = "$#&*$"

	menu = f"Você escolheu VISUALIZAR os comentários a respeito do centro de saúde: {nome_indice}\n"

	opcao = 1

	while opcao < 0 or opcao > 0:
		clear()
		print(menu)
		for linha in comentarios:
			print("\n-> "+linha)
		opcao = int(input("\n\nPara voltar digite 0 (zero): "))

	info_center(indice)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

start()
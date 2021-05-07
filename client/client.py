import os
import sqlite3
import requests
import time
import json

# con = sqlite3.connect("banco.db")#cria a base/banco de dados caso não exista.
# cursor = con.cursor()#abrindo conexao
host = "http://127.0.0.1:8000"

def start():
	clear()
	menu_principal = ("Bem vindos ao ComunicHealth, o que deseja fazer: \n\n"
			"1 - Lista de centros de saúde\n"
			"2 - Ajuda\n"
			"0 - Sair \n")

	print(menu_principal)
	opcao = int(input("Escolha uma opção (ex: 1): "))

	if opcao == 1:
		list_centers()
	if opcao == 2:
		clear()
		print("Ainda está sendo desenvolvido...")
		time.sleep(3)
		start()
	if opcao == 0:
		clear()
		print("Obrigado por utilizar o CommunicHealth <3")
		exit()
	else:
		start()

def list_centers():
	# pegariamos a lista de nomes e os indices de cada centro cadastrado

	lista = {
		"indice": [],
		"nome": []
	}

	# cursor.execute("SELECT indice,nome FROM centers;")
	url = host+"/get/vars/indice/nome"
	res = requests.get(url)
	obj = res.json()

	# print(type(cursor.fetchall))
	for index in range(len(obj["indices"])):
		lista["indice"].append(obj["indices"][index])
		lista["nome"].append(obj["nomes"][index])

	menu_centers = "Escolha um centro médico cadastrado:\n\n"
	contador = 0
	escolhas = ""

	for indice in range(len(lista["indice"])):
		clear()
		atual_indice = lista["indice"][indice]
		atual_nome = lista["nome"][indice]
		escolhas += f"{atual_indice} - {atual_nome}\n"
	escolhas += "\n0 - Voltar"
	menu_centers += escolhas
	
	opcao = -1

	# print(lista["indice"][-1])

	while opcao < 0 or opcao > lista["indice"][-1]:
		clear()
		print(menu_centers)
		opcao = int(input("Escolha um centro de saúde (ex: 1): "))

		if opcao == 0:
			clear()
			print("Obrigado por utilizar o CommunicHealth <3")
			start()
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


	url = host+"/get/vars/indice/nome/localizacao/avaliacao/"+str(indice)
	res = requests.get(url)
	obj = res.json()

	# cursor.execute(f"SELECT * FROM centers WHERE indice == {indice}")

	# print(obj)
	for linha in range(len(obj["indices"])):
		lista["indice"] = obj["indices"][0]
		lista["nome"] = obj["nomes"][0]
		lista["nota_avaliacao"] = obj["nota_avaliacao"][0]
		lista["localizacao"] = obj["localizacao"][0]

	# print(lista)
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

	url = host+"/get/vars/indice/nome/comentarios/"+str(indice)
	res = requests.get(url)
	obj = res.json()

	lista["indice"] = obj["indices"][0]
	lista["nome"] = obj["nomes"][0]
	lista["lista_coments"] = obj["lista_coments"][0]

	nome_indice = lista["nome"]
	separator = "$#&*$"

	menu = f"Você escolheu fazer um comentário sobre o centro de saúde: {nome_indice}"

	print(menu)

	comentario = input("\n\nDigite um comentário sobre (ex: Gostei muito do lugar, bem organizado...): ").strip()
	comentario = (lista["lista_coments"]+separator+comentario)

	send_obj = {
		"indice": indice,
		"lista_coments": comentario
	}
	url = host+"/add/vars/comentarios"
	res = requests.post(url, data=json.dumps(send_obj))

	print(res)
	# cursor.execute(f"UPDATE centers SET lista_coments = '{comentario}' WHERE indice = '{indice}'")
	# con.commit()
	time.sleep(4)
	clear()
	
	print("Comentário adicionado com sucesso: ")
	time.sleep(2)

	info_center(indice)


def ver_coments(indice):
	#baseado no indice carregar todos comentários do centro de saúde.
	lista = {
		"indice": 0,
		"nome": "",
		"lista_coments" : ""
	}

	url = host+"/get/vars/indice/nome/comentarios/"+str(indice)
	res = requests.get(url)
	obj = res.json()

	# cursor.execute(f"SELECT * FROM centers WHERE indice == {indice}")

	lista["indice"] = obj["indices"][0]
	lista["nome"] = obj["nomes"][0]
	lista["lista_coments"] = obj["lista_coments"][0]

	comentarios = lista["lista_coments"].split("$#&*$")

	nome_indice = lista["nome"]

	menu = f"Você escolheu VISUALIZAR os comentários a respeito do centro de saúde: {nome_indice}\n"

	opcao = 1

	while opcao < 0 or opcao > 0:
		clear()
		print(menu)
		for linha in comentarios[1:]:
			print("\n-> "+linha)
		opcao = int(input("\n\nPara voltar digite 0 (zero): "))

	info_center(indice)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

start()
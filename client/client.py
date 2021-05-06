import os

#request

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
		"nome": ['Getúlio Vargas', 'Posto da Vila União', 'Outros'],
		"indice": [0, 1, 2]
	}

	clear()

	menu_centers = "Escolha um centro médico cadastrado:\n\n"
	contador = 0
	escolhas = ""

	for indice in range(len(lista["indice"])):
		atual_indice = lista["indice"][indice]
		atual_nome = lista["nome"][indice]
		escolhas += f"{atual_indice} - {atual_nome}\n"

	menu_centers += escolhas
	
	opcao = -1

	# print(lista["indice"][-1])

	while opcao < 0 or opcao > lista["indice"][-1]+1:
		clear()
		print(menu_centers)
		opcao = int(input("Escolha um centro de saúde (ex: 1): "))

	info_center(opcao)

def info_center(indice):
	
	# aqui vai ficar o acesso a api e retornar os dados do hospital.
	# - Indice
	# - Nome 
	# - Nota de avaliação
	# - Lista de comentários

	valores = {
		"indice": 0,
		"nome": "",
		"nota_avaliacao": 0.0,
		"lista_coments": []
	}

	infos = (""
		""
		"\n\n")

	escolha = "1 - Ver comentários \n2 - Adicionar comentário \n3 - Voltar\n\n"

	opcao = -1

	while opcao < 0 or opcao > 3:
		clear()

		print(infos)

		print(escolha)

		opcao = int(input("Escolha uma ação (ex: 1): "))

		if opcao == 1:
			ver_coments(valores["indice"])
		if opcao == 2:
			adc_coments(valores["indice"])
		if opcao == 3:
			list_centers()

	
def adc_coments(indice):
	clear()
	# pesquisar nome do escolhido

	# print(indice)

	nome_indice = "DEFAULT"
	
	menu = f"Você escolheu fazer um comentário sobre o centro de saúde: {nome_indice}"

	print(menu)

	comentario = input("\n\nDigite um comentário sobre (ex: Gostei muito do lugar, bem organizado...): ")
	comentario += (comentario+"\n\n")

	clear()
	print("Comentário adicionado com sucesso: ")

	info_center(indice)

	# popular comentário

def ver_coments(indice):
	#baseado no indice carregar todos comentários do centro de saúde.
	comentarios = "aaaa"

	opcao = 1

	while opcao < 0 or opcao > 0:
		clear()
		print(comentarios)
		opcao = int(input("\n\nPara voltar digite 0 (zero): "))

	info_center(indice)

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

start()
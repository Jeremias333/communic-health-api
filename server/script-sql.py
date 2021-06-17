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
	
 	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Correia Picanço', 5.0, 'Rua Padre Roma, 149 Tamarineira Recife - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Geral de Areias', 5.0, 'Avenida Recife, 810 - Estância Recife - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Colônia Professor Alcides Codeceira', 5.0, 'Avenida Barão de Vera Cruz, S/N Cruz de Rebouças Igarassu - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Jaboatão Prazeres', 5.0, 'Rua Recife, S/N Cajueiro Seco Jaboatão dos Guararapes - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Metropolitano Norte – Miguel Arraes de Alencar', 5.0, 'Estrada da Fazendinha, S/N Jaguaribe Paulista - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Metropolitano Oeste – Pelópidas Silveira', 5.0, 'BR 232, Km 06 Curado Recife - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Metropolitano Sul – Dom Hélder Câmara', 5.0, 'BR 101 Sul - Km 28 Cabo de Santo Agostinho - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Otávio de Freitas', 5.0, 'Rua Aprígio Guimarães, S/N - Tejipió Recife - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('Hospital Psiquiátrico Ulysses Pernambucano', 5.0, 'Avenida Rosa e Silva, 2.130 Tamarineira Recife - PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Olinda – Gregório Lourenço Bezerra', 5.0, 'Rodovia PE15 – Avenida Joaquim Nabuco, S/N, Cidade Tabajara – Olinda/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Igarassu – Honorata de Queiroz Galvão', 5.0, 'Rodovia BR-101Norte, KM47, Centro – Igarassu/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Paulista – Geraldo Pinho Alves', 5.0, ' Estrada do Frio, 1000 – Aurora – Jardim Paulista - Paulista/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Imbiribeira – Maria Esther Souto Carvalho', 5.0, 'Avenida Mascarenhas de Moraes, ao lado do 4.202, Imbiribeira – Recife/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA São Lourenço da Mata – Professor Fernando Figueira', 5.0, 'Avenida Dr. Francisco Correia, 2.009, Pixete – São Lourenço da Mata/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Curado – Médico Fernando de Lacerda', 5.0, 'Avenida Leonardo da Vinci, 68, Curado II – Jaboatão dos Guararapes/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Barra de Jangada – Wilson Campos', 5.0, 'Rua Cruz Alta, S/N – Barra de Jangada (de frente à estação da Compesa) – Jaboatão dos Guararapes/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Engenho Velho – Carlos Wilson', 5.0, ' Rua General Manoel Rabelo, S/N (na altura da penúltima estação do metrô, a de Engenho Velho) – Jaboatão dos Guararapes', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('UPA Cabo de Santo Agostinho – Deputado Francisco Julião', 5.0, ' Rua Paulo Manoel da Cunha, nº 830, Núcleo Residencial Ministro Marcos Freire -  Cohab – Cabo de Santo Agostinho/PE', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 326 USF JADER DE ANDRADE COMUNIDADE ENTRA APULSO', 5.0, 'RUA CEL ANIZIO RODRIGUES COELHO - 8, CEP: 51021130 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 243 USF SANTO AMARO II', 5.0, 'RUA BUARQUE DE MACEDO - 65, CEP: 50110340 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 255 USF UPINHA 24H VILA ARRAES', 5.0, 'RUA GEN ADAUTO GOMES BARBOSA - 13, CEP: 50741280 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 280 USF SITIO CARDOSO', 5.0, 'RUA PADRE LANDIM - 342, CEP: 50710485 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 397 USF UPINHA DIA CORREGO DO EUCLIDES', 5.0, 'RUA CORREGO DO EUCLIDES - 309, CEP: 52080001 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 337 USF SITIO WANDERLEY', 5.0, 'RUA HEMETRIO MACIEL - 311, CEP: 50740120 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 126 CS VER ROMILDO GOMES', 5.0, 'RUA JALISCO - S/N, CEP: 51150460 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 284 USF VILA SAO MIGUEL MARROM GLACE', 5.0, 'RUA MARIAPOLIS - 132, CEP: 50770640 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 248 USF BARREIRAS', 5.0, 'RUA AGUA CLARA - 145, CEP: 50980160 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 239 USF COQUEIRAL I E II', 5.0, 'RUA MARIA TERESA - 174, CEP: 50791280 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 154 USF UPINHA DIA RIO DA PRATA', 5.0, 'RUA RIO PAJEU - S/N, CEP: 51230360 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 142 CS BIDU KRAUSE', 5.0, 'AV ONZE DE AGOSTO - S/N, CEP: 50791465 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 292 USF VILA DO IPSEP', 5.0, 'RUA VIRGINIA HERACLIO - S/N, CEP: 51350250 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 222 USF CORREGO DO CURIO', 5.0, 'RUA CORREGO DO CURIO - 43, CEP: 52150160 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 155 CS PROF MONTEIRO DE MORAIS', 5.0, 'AV BEBERIBE - 4510, CEP: 52130000 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 271 PSF TASSO BEZERRA CHIE II', 5.0, 'RUA GUAIANAZES - 379, CEP: 52031300 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 336 USF UNIAO DAS VILAS', 5.0, 'AV AGAMENON MAGALHAES - 2901, CEP: 52020000 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 171 CS JOAQUIM COSTA CARVALHO', 5.0, 'RUA SIRIJI - S/N, CEP: 52130110 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 267 USF UR 2', 5.0, 'AV SANTA FE - 240, CEP: 51340240 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 338 USF UPINHA DIA JARDIM SAO PAULO', 5.0, 'PRACA JARDIM SAO PAULO - S/N, CEP: 50781760 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 334 USF CABANGA', 5.0, 'RUA ESCRITOR SOUZA BARROS - S/N, CEP: 50090410 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 183 USF SITIO DOS MACACOS', 5.0, 'ESTRADA DOS MACACOS - 47, CEP: 52171215 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 187 USF ILHA DE DEUS', 5.0, 'RUA SAO JOSE - S/N, CEP: 51150192 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 289 USF JOSUE DE CASTRO', 5.0, 'AV CORACAO DE JESUS - S/N, CEP: 51345205 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 221 USF ILHA DE JOANEIRO', 5.0, 'RUA MARECHAL DEODORO - 688, CEP: 52031440 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 225 USF SKYLAB II', 5.0, 'RUA ITAPIRANGA - 791, CEP: 50680210 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 291 USF ALTO DOS COQUEIROS CORREGO DA JAQUEIRA', 5.0, 'RUA CORREGO DA JAQUEIRA - 160, CEP: 52131140 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 344 USF JIQUIA I E II', 5.0, 'RUA PADRE ROQUE - 33, CEP: 50771380 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 240 USF COELHOS I', 5.0, 'RUA BITURUNA - 110, CEP: 50060000 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 287 USF ALTO JOSE DO PINHO', 5.0, 'RUA MARAGOGI - 5, CEP: 52210120 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 150 CS PROFESSOR FERNANDES FIGUEIRAS', 5.0, 'AV SAO PAULO - 605, CEP: 50910250 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 226 USF CHAO DE ESTRELAS', 5.0, 'RUA DR ELIAS GOMES - 65, CEP: 52121220 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 173 USF DANCING DAYS', 5.0, 'RUA DANCING DAYS - 109, CEP: 51180340 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 300 USF DR GERALDO BARRETO CAMPELO SAN MARTIN', 5.0, 'RUA COMENDADOR FRANCO FERREIRA - S/N, CEP: 50761310 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 230 USF LAGOA ENCANTADA', 5.0, 'AV BENIGNO JORDAO DE VASCONCELOS - S/N, CEP: 51280400 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 218 USF COQUE', 5.0, 'RUA GUAPIRAMA - 65, CEP: 50080730 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 265 USF MANGUEIRA I', 5.0, 'RUA JUPIACARA - 70, CEP: 50761610 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 168 CTA CENTRO DE TESTAGEM E ACONSELHAMENTO', 5.0, 'LARGO DA SANTA CRUZ - S/N, CEP: 50060220 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 137 CS PROF DJAIR BRINDEIRO', 5.0, 'RUA COSMORAMA - S/N, CEP: 51030640 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 113 CS DR ARISTARCO AZEVEDO', 5.0, 'RUA BAHIA - 29, CEP: 51250370 Boa Vista - Recife', '');")
	cursor.execute("INSERT INTO centers (nome, nota_avaliacao, localizacao, lista_coments) VALUES ('US 138 USF DR LUIZ WILSOM', 5.0, 'RUA CHA DE ALEGRIA - S/N, CEP: 52211130 Boa Vista - Recife', '');")
	
 	cursor.execute("INSERT INTO users (username, email, password, favorites) VALUES ('jeremias333', 'jeremais@cummunichealth.com', '123456', '[1,2,3]');")
	con.commit()

initial()
insert_default()
con.close()
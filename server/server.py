from typing import Optional
from fastapi import FastAPI, Request
import access
import json

app = FastAPI()

@app.get("/get/all")
def get_all():
	return access.get_all()

@app.get("/get/vars/indice/nome")
def get_id_name():
	return access.get_id_name()

@app.get("/get/vars/indice/nome/comentarios/{indice}")
async def get_id_name_coments(indice):
	indice = int(indice[0])
	return access.get_id_name_coments(indice)

@app.get("/get/vars/indice/nome/localizacao/avaliacao/{indice}")
async def get_id_name_localization_rate(indice):
	indice = int(indice[0])
	return access.get_id_name_localization_rate(indice)
#data_dict = {
#	"indice": 1,
#	"comentario": "aaaaa"
#}

#r = requests.post('http://127.0.0.1:8000/add/vars/comentarios', data=json.dumps(data_dict))
@app.post("/add/vars/comentarios")
async def add_comments(request: Request):
	obj = await request.body()
	# obj = await request.bo
	obj_dict = json.loads(obj)
	print(obj_dict)
	print(type(obj_dict))
	return access.add_comments(obj=obj_dict)


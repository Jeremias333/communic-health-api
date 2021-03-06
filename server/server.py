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

@app.get("/get/vars/rating")
def get_id_name():
	return access.get_id_name_rating()

@app.get("/get/vars/address")
def get_id_address():
    return access.get_id_name_address()

@app.get("/get/vars/indice/nome/comentarios/{indice}")
async def get_id_name_coments(indice):
	indice = int(indice)
	return access.get_id_name_coments(indice)

@app.get("/get/vars/indice/nome/localizacao/avaliacao/{indice}")
async def get_id_name_localization_rate(indice):
	indice = int(indice)
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

@app.post("/signup")
async def add_user(request: Request):
	obj = await request.body()
	obj_dict = json.loads(obj)
	print(obj_dict)
	return access.add_user(obj_dict)

@app.post("/login")
async def login(request: Request):
	obj = await request.body()
	obj_dict = json.loads(obj)
	print(obj_dict)
	return access.do_login(obj_dict)

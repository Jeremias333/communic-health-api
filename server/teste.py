import requests
import json

data_dict = {
	"indice": 1,
	"comentario": "aaaaa"
}

r = requests.post('http://127.0.0.1:8000/add/vars/comentarios', data=json.dumps(data_dict))
# r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# print(type(r.text))
# print(r.json())

obj = r.json()

print(obj)

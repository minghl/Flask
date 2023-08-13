import requests

# res = requests.get('http://127.0.0.1:5000/hello/')
res = requests.post('http://127.0.0.1:5000/hello/')
# res = requests.put('http://127.0.0.1:5000/users/')
# res = requests.delete('http://127.0.0.1:5000/users/')
print(res.text)
import requests
# pip install requests

# GET 请求
res = requests.get('http://127.0.0.1:5000/request/?name=lisi&age=33', cookies={'name':'hello'})
print(res.text)

# POST 请求
# res = requests.post('http://127.0.0.1:5000/request/',data={'name':'lucy','age':18})
# print(res.text)
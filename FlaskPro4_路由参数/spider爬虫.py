import requests
# pip install requests

# GET 请求
res = requests.post('http://127.0.0.1:5000/methods/')
print(res.text)
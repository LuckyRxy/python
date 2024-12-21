# todo: requests库练习
#
# @Time: 2024/12/21 16:43:43
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import requests


"""
@todo: GET请求
@return: 
"""
resp = requests.get("https://jsonplaceholder.typicode.com/posts")

print(resp.status_code)
print(resp.text)
print(len(resp.json()))

"""
@todo: 通过params参数再url中附加查询参数
@return: 
"""
params = {'userId':1}
resp = requests.get("https://jsonplaceholder.typicode.com/posts",params=params)

print(resp.status_code)


"""
@todo: POST请求
@return: 
"""
url = "https://jsonplaceholder.typicode.com/posts"
data = {'title':'foo','body':'bar','userId': 1}
resp = requests.post(url,json=data)

print(resp.status_code)
print(resp.json())

"""
@todo: 文件上传
@return: 
"""
file = {'file':open('./data/example.txt', 'rb')}
resp = requests.post('https://httpbin.org/post',files=file)

print(resp.json())


"""
@todo: 可以用于跨多个请求保持会话状态（例如 Cookies、请求头等）
@return: 
"""
session = requests.Session()
session.headers.update({'User-Agent': 'my-app'})

# 第一次请求
resp = session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print(resp.cookies)

# 第二次请求， cookies会被自动发送
resp = session.get('https://httpbin.org/cookies')
print(resp.json())


"""
@todo: 设置请求超时时间
@return: 
"""
try:
    resp = requests.get('https://httpbin.org/delay/5',timeout=3) # 设置请求时间为3s
except Exception as e:
    print('请求超时')



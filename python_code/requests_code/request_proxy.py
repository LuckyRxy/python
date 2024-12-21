# todo: 可以通过代理访问网络（例如爬虫场景中使用代理池）
#
# @Time: 2024/12/21 19:13:15
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import requests

# 代理设置
proxies = {
    'http': 'http://localhost:8080', # 表示所有 HTTP 请求会通过 http://localhost:8080 代理
    'https': 'http://localhost:8080', # 表示所有 HTTPS 请求会通过 http://localhost:8080 代理
}

# 发起请求，使用代理
response = requests.get('https://httpbin.org/ip', proxies=proxies)

# 打印响应内容
print(response.text)

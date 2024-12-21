# todo: 通过 requests.adapters 和 urllib3 实现请求重试功能
#
# @Time: 2024/12/21 18:59:41
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 创建会话
session = requests.Session()

# 设置重试策略
# backoff_factor: backoff_factor 控制重试间隔的增长模式，通常是指数增长。
# 具体而言，如果 backoff_factor 为 1，第一次重试的间隔是 1 秒，第二次是 2 秒，第三次是 4 秒，
# 依此类推。这个值可以帮助避免在高负载情况下频繁请求造成的资源浪费。
retries = Retry(
    total=3, # 设置最大重试次数为 3 次
    backoff_factor=1, # 设置重试的间隔时间的增量因子
    status_forcelist=[500,502,503,504]
)
adapter = HTTPAdapter(max_retries=retries)

# 为会话挂载适配器,使得所有以 http://和https:// 开头的请求都使用这个适配器
session.mount('http://', adapter)
session.mount('https://', adapter)

resp = session.get('https://httpbin.org/status/500')
print(resp.status_code)
"""
练习：HTTP 请求

描述：
本练习帮助您学习如何使用 requests 库发送 HTTP 请求并处理响应。
注意：运行此练习前，请确保已安装 requests 库（pip install requests）。

请补全下面的函数，实现发送 HTTP 请求并处理响应的功能。
"""
import re

import requests


def get_website_content(url):
    """
    发送 GET 请求获取网页内容
    
    参数:
    - url: 目标网站 URL
    
    返回:
    - 包含响应信息的字典：
      {
        'status_code': HTTP 状态码，
        'content': 响应内容文本，
        'headers': 响应头部信息
      }
    """
    # 请在下方编写代码
    # 使用 requests.get() 发送 GET 请求
    # 返回包含状态码、内容和头部信息的字典
    response = requests.get(url)
    info = {}
    info['status_code'] = response.status_code
    info['content'] = response.text
    info['headers'] = response.headers
    return info

def post_data(url, data):
    """
    发送 POST 请求提交数据
    
    参数:
    - url: 目标网站 URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP 状态码，
        'response_json': 响应的 JSON 数据 (如果有),
        'success': 请求是否成功 (状态码为 2xx)
      }
    """
    # 请在下方编写代码
    # 使用 requests.post() 发送 POST 请求
    # 返回包含状态码、响应 JSON 和成功标志的字典
    response = requests.post(url, data=data)
    info = {}
    info['status_code'] = response.status_code
    info['response_json'] = response.json()
    info['success'] = response.ok
    return info
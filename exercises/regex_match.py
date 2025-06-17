"""
练习：正则表达式匹配

在本练习中，你将练习使用 Python 的正则表达式来处理文本匹配和提取。
"""
import re

def find_emails(text):
    """
    从文本中提取所有的电子邮件地址。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有电子邮件地址的列表
    """
    # 实现你的代码：使用正则表达式查找所有邮箱地址
    # 邮箱格式通常为：username@domain.com
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def is_valid_phone_number(phone):
    """
    验证字符串是否为有效的中国手机号码。
    有效的手机号码应该:
    1. 长度为 11 位
    2. 以 1 开头
    3. 第二位是 3-9 之间的数字
    4. 全部由数字组成
    
    参数:
        phone (str): 要验证的电话号码字符串
        
    返回:
        bool: 如果是有效的手机号码则返回 True，否则返回 False
    """
    # 实现你的代码：验证手机号码是否合法
    phone_pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(phone_pattern, phone))

def extract_urls(text):
    """
    从文本中提取所有的 URL 链接。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有 URL 的列表
    """
    # 实现你的代码：使用正则表达式提取所有 URL
    # 需要考虑 http://和 https://开头的 URL
    url_pattern = r'https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?'
    return re.findall(url_pattern, text)
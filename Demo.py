import re
import requests
import parsel


string = """
2b2b2b2b2b2b2b21a1a1a1a1a1a1a1
"""
# 提取b 替换的内容
img_url_list = re.findall('2(.*?)2', string)
# 提取a 需要替换的内容
img_list = re.findall('1(.*?)1', string)
for img, img_url in zip(img_list, img_url_list):
    string = string.replace(img, img_url)

print(img_url_list, img_list)
print(string)


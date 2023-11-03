"""
代码实现步骤
1，发生请求，模拟游览器对于URL地址发送请求
    请求链接<数据包>:https://www.zhihu.com/people/wu-en-da-89
2,获取数据，获取服务器返回相应数据
    开发者工具：response
3,数据解析，提取我们想要的数据
    数据：文章标题 文章内容
4，保存数据，把文章转换成PDF
    -先保存成功HTML文件
    -通过HTML文件转换成PDF
"""
# from _ast import pattern

# 导入数据请求模块
import requests
# 导入正则模块
import re
# 导入数据解析模块
import parsel

"""
1，发送请求，模拟游览器对于URL地址发送请求
    请求链接<数据包>:https://www.zhihu.com/people/wu-en-da-89

调用requests 模块里get请求方法,对于url地址发送请求, 并且携带上headers请求头伪装
      
response = requests.get(url=url, headers=headers)
    - requests -> 数据请求模板
    - get() -> requests里面的请求方法 <根据开发者工具选择>
    - url=rul, headers=hears -> 往get请求函数里面传参
        左边: url / headers get函数里面形式参数
        右边: url / headers 我们传入进去链接地址和请求头
    - response 自定义变量名, 用于接受等号右边的内容
"""

# 模拟游览器
headers = {
    # User-Agent 用户代理，表示游览器基本身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36'
}
# 请求链接
url = 'https://zhuanlan.zhihu.com/p/55460915'
# 发送请求 <Response [200]> 响应对象
response = requests.get(url=url, headers=headers)
# 2. 获取响应文本数据
html_data = response.text
"""
3. 解析数据, 提取我们需要的数据内容
    数据: 文章标题 文章内容
    
调用re模块findall方法
- re.findall('数据', '数据源') -> 找到所有你想要的数据
数据: 你需要的数据内容
数据源: 从什么地方能获取这个数据
    title = re.findall('<title data-rh="true">(.*?)</title>', html_data)

CSS选择器 / Xpath节点提取<根据标签属性/截取内容>
    -把获取到HTML字串数据,转成可以解析对象
"""
# 通过CSS 选择器提取数据 需要把获取到的HTML字符串数据,转换成可以解析的对象
selector = parsel.Selector(html_data)
# 标题
title = selector.css('.Post-Title::text').get()
# title = re.findall('<title data-rh="true">(.*?)</title>', html_data)
# 文章内容 <html标签>
content = selector.css('.css-376mun .RichText').get()
"""
4,保持数据, 把文章保存为PDF
"""
# 前端模板
html_str = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
{article}
</body>
</html>
'''
# 使用正则匹配图片链接
img_url_list = re.findall('<noscript><img src="(.*?)" data-caption=""', content)
# 提取需要被替换的内容
img_list = re.findall('</noscript><img src="(.*?)" data-caption=""', content)
# print(img_url_list)
# print(img_list)
for img, img_url in zip(img_list, img_url_list):
    print(img)
    print(img_url)
content = content.replace(img, img_url)
print(content)
print(img_url_list)
print(img_list)

# 字符串格式化方法
html = html_str.format(article=content)
html_file = 'html\\{title}.html'.format(title=title)
html_file = f'html\\{title}.html'
# 保存HTML文件
with open(html_file, mode='w', encoding='utf-8') as c:
    c.write(html)
# print(response)
# print(html_data)
print(title)
print(content)
print(html)

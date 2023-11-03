"""
[课程内容]: Python采集知乎专栏文章保存成pdf

[授课老师]: 青灯教育-自游  20: 05正式开始讲课 可以点歌 可以问问题

[环境使用]:
    Python 3.8
    Pycharm
    wkhtmltopdf 软件  找木子老师获取

[模块使用]:
    requests >>> pip install requests  数据请求
    parsel >>> pip install parsel  数据解析
    re >>> 内置模块 不需要安装 正则表达式
    pdfkit >>> pip install pdfkit

---------------------------------------------------------------------------------------------------
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学, 20: 05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信
---------------------------------------------------------------------------------------------------
零基础同学 -> 0
有基础同学 -> 1

爬虫基本流程: <爬虫程序基本公式>

一. 数据来源分析
    1. 明确需求
        - 明确采集网站以及数据内容
            网址: https://zhuanlan.zhihu.com/p/193129156
            数据: 文章内容 / 文章标题
    2. 抓包分析
        - 通过开发者工具进行抓包分析
        I. 打开开发者工具: F12 / 右键点击检查选择network
        II. 刷新网页: 让网页数据内容重新加载一遍
        III. 通过关键搜索找到数据对应的数据链接<数据包>
            数据包: https://zhuanlan.zhihu.com/p/193129156

二. 代码实现步骤
    1. 发送请求, 模拟浏览器对于url地址发送请求
        请求链接<数据包>: https://zhuanlan.zhihu.com/p/193129156
    2. 获取数据, 获取服务器返回响应数据
        开发者工具: response
    3. 解析数据, 提取我们需要的数据内容
        数据: 文章标题 文章内容
    4. 保存数据, 把文章内容保存成pdf
        - 先保存成功html文件
        - 通过html文件转成PDF文件

需要流程笔记的同学 --> 加木子老师自行领取

1. 喜欢边听边写
2. 喜欢课后看录播在写代码 --> 加木子老师课后自行领取
    中途早退的同学, 是没有录播的 <温馨提示>

多页数据采集:
    分析请求链接变化规律
        - 请求链接: 文章链接
    https://zhuanlan.zhihu.com/p/193129156
    https://zhuanlan.zhihu.com/p/191602133
    https://zhuanlan.zhihu.com/p/191600009

每篇文章都有一个ID --> 所有专栏<整个网站>文章ID

本届案例难度:
    相当于学习过一周左右同学水平 <基础三节课, 爬虫三节课>
for循环
字典创建
字符串定义
变量名定义
字符串格式化 替换
文件操作

requests模块 re模块 parsel模块


从零基础如何去学习:
    自学:
        时间成本, 效率
    - 资料选择, 不断去筛选 <老师风格 / 教授知识点是否符合>
    - 问题解决时间成本

    报班:

学习编程:
    想要成为行业最牛逼那一批人, 可以的

主要目的:
    实现技术变现 -> 接外包 / 就业工作

接外包:
    学习方向: 核心编程 爬虫开发 数据分析
    学习效果:
        正常2个月左右时间, 学完爬虫之后, 是可以接单

就业工作:
    学习方向: 核心编程 爬虫开发 数据分析 网站开发 人工智能
    学习效果:
        6-7个月左右, 学完80%左右知识点,你可以达到企业开发水平


课程服务:
    - 直播授课
        一周三节课, 晚上20-22
    - 课后录播 源码 笔记 文档 软件工具 作业 考核
    - 老师解答辅导
    - 班主任监督学习, 电话通知听课
    - 免费重修, 学N次
    - 外包指导
    - 就业指导
    - 培训合同
    - 发票
    - 毕业证书
    ...

包教包会, 前提:
    按时听课: 坚持学习
    按时完成作业: 多敲多练
    认真学习态度: 不懂多问
老师可以保证你能够学会掌握

违法:
    涉及版权问题 隐私问题 用户信息 国家信息....

课程学费:
直播+录播
    核心编程: 2260
    爬虫开发: 2980
    数据分析: 2180
    网站开发: 2980
学费: 10400
专题录播:
    自动化办公: 1680
    人工智能: 2680
学费: 4360

总计学费: 14760

想要报名课程加清风老师微信: pythonmiss
    预定300元学费
享有七夕活动节
    活动一: 爱心红包, 学费减免
        一. 高薪就业课程: 核心编程 爬虫开发 数据分析 网站开发
            原价学费: 10400 - 1314 - 520 - 300<预定学费> = 8266
            额外免费赠送:
                价值4360元 自动化办公+人工智能课程
        二. 兼职外包课程: 核心编程 爬虫开发 数据分析
            原价学费: 7420 - 520 - 520 - 300 = 6080
            额外免费赠送:
                价值1680元自动化办公
    活动二: 分期免息学习 0利息0手续费
        经济条件有限, 学习压力降低 3/6/9/12/18/24 分期免息学习课程内容
            8266 / 12 = 688
            8266 / 18 = 459
            8266 / 24 = 344

        6080 / 12 = 506
        6080 / 18 = 337

课程价值 --> 学习技术知识点 + 老师教学服务

今天预定300元学费, 直接进班学习
    9月23号, 支付第一个月学费 344 元 <平均12元左右>
        课程资料 源码 录播 老师解答辅导
    10月23号, 支付第二个月学费 344 元 <平均12元左右>

学完爬虫之后, 还可以接单 --> 接单问题还可以解答辅导


"""
# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入数据解析模块
import parsel
import pdfkit

"""
1. 发送请求, 模拟浏览器对于url地址发送请求
    请求链接<数据包>: https://zhuanlan.zhihu.com/p/193129156

调用requests模块里get请求方法, 对于url地址发送请求, 并且携带上headers请求头伪装
    最后用自定义变量response接收返回数据
response = requests.get(url=url, headers=headers)
    - requests -> 数据请求模块
    - get() -> requests里面请求方法 <根据开发者工具来选择>
    - url=url, headers=headers -> 往get请求函数里面传参
        左边: url / headers get函数里面形式参数
        右边: url / headers 我们传入进去链接地址和请求头
    - response 自定义变量名, 用于接受等号右边的内容
"""
# 模拟浏览器
headers = {
    # User-Agent 用户代理, 表示浏览器基本身份信息
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
for page in range(0, 50, 10):
    link = f'https://www.zhihu.com/api/v4/columns/c_1090924073042837504/items?limit=10&offset={page}'
    json_data = requests.get(url=link, headers=headers).json()
    for index in json_data['data']:
        # 请求链接
        url = f'https://zhuanlan.zhihu.com/p/{index["id"]}'
        # 发送请求 <Response [200]> 响应对象
        response = requests.get(url=url, headers=headers)
        # 2. 获取响应文本数据
        html_data = response.text
        """
        3. 解析数据, 提取我们需要的数据内容
            数据: 文章标题 文章内容
        正则表达式: 可以直接提取字符串里面数据内容
            调用re模块findall方法
            - re.findall('数据', '数据源') -> 找到所有你想要的数据
                数据: 你需要的数据内容
                数据源: 从什么地方能够获取这个数据
                    title = re.findall('<title data-rh="true">(.*?) - 知乎</title>', html_data)
        
        css选择器 / xpath节点提取 <根据标签属性/节点提取数据内容>
            - 把获取到html字符串数据, 转成可解析对象
        """
        # 通过css选择器提取数据 需要把获取到html字符串数据, 转成可解析对象
        selector = parsel.Selector(html_data)
        # 标题
        title = selector.css('.Post-Title::text').get()
        # 替换特殊字符
        title = re.sub(r'[\\/"*<>:?|]', '', title)
        # 文章内容 <html标签>
        content = selector.css('.css-376mun .RichText').get()
        """
        4. 保存数据, 把文章内容保存成pdf
        """
        # 前端模板
        html_str ='''
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
        # 提取图片链接
        img_url_list = re.findall('<noscript><img src="(.*?)" data-caption=""', content)
        # 提取需要被替换的内
        img_list = re.findall('</noscript><img src="(.*?)" data-caption=""', content)
        # for循环遍历, 把列表里面的元素一个一个提取出来
        for img, img_url in zip(img_list, img_url_list):
            # 字符串替换方法, 把img 替换成 img_url
            # 把 'data:image/svg+xml;utf8,...' 替换成 https://pic1.zhimg.com/v2-8ff79324ee6011071769664dd4d6fdac_b.jpg
            content = content.replace(img, img_url)
        # 字符串格式化方法
        html = html_str.format(article=content)
        html_file = f'html\\{title}.html'
        pdf_file = f'pdf\\{title}.pdf'
        # 保存html文件
        with open(html_file, mode='w', encoding='utf-8') as c:
            c.write(html)

        # 把html文件转成pdf --> wkhtmltopdf 软件
        # config = pdfkit.configuration(wkhtmltopdf=r'D:\demo\wkhtmltopdf\bin\wkhtmltopdf.exe')
        config = pdfkit.configuration(wkhtmltopdf=r'D:\wkhtmltopdf\bin\wkhtmltopdf.exe')
        pdfkit.from_file(html_file, pdf_file, configuration=config)
        print(title)


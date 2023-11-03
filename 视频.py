"""
[课题]: Python实战 | 如何抓取腾讯视频

[介绍]: 一键下载视频

[授课老师]: 青灯教育-巳月     [上课时间]: 20:05

[环境介绍]:
	python 3.8
	pycharm
	requests >>> pip install requests
	tqdm >>> pip install tqdm

先听一下歌, 等一下后面进来的同学, 20:05开始讲课 有什么喜欢听的歌 也可以发在公屏上

[没听懂?]
课后的回放录播资料小钰老师微信
+python安装包 安装教程视频
+pycharm 社区版  专业版 及 激活码免费

零基础 0
    1. 不要跟着我敲代码, 先听思路 把思路听懂之后 课后领取录播 去实现代码
    2. 思路上有任何问题的时候 一定要记得及时提问
有基础 1

什么是爬虫?
    作用: 采集数据(视频/图片/文本/音频) / 模拟用户行为(点赞/评论/浏览量/下单/抢购...)
    原理: 模拟成 客户端 向 服务器 发送网络请求

我们需要采集视频
    视频格式: 腾讯视频/爱奇艺/芒果tv ...
        m3u8视频流的格式
    m3u8: 文本文件 里面存储的是 所有的片段视频的链接
    找到这个 .m3u8 文件即可

数据来源:
https://vd6.l.qq.com/proxyhttp

代码实现思路:
    1. 访问数据来源
    2. 取到整个数据
    3. 将需要的 m3u8 文本内容 提取出来
    4. 将其中的 所有的ts片段视频链接 取到
    5. 将每个ts片段链接拼接好
    6. 挨个访问 并保存为一个视频

没有会员怎么处理的思路
    爬盗版网站
    爬虫不能破解
ts链接的问题


如果以后不用来 工作/兼职 那么你这一小时 就是白听了

找工作 1
    技术:
        核心编程
        爬虫开发
        数据分析
        网站开发
    学历:
        问题不是很大, 大专 也可以 中专 有点危险 但有机会
    找工作:
        推荐去 一线城市 (北上广深杭)
            福利待遇会好一些, 能够给到你的锻炼的机会也会更多
        掌握 80%以上 8-15k 薪资区间 是问题不大的
做副业 2
    技术: 外包会比较多
        核心编程
        爬虫开发
        数据分析
    渠道:
        1. 猿急送 / 程序员客栈 等 外包平台找外包 (有一定难度, 做不出来 会扣钱)
        2. 找小平台 淘宝 找商家 / QQ群 / 微信群 (防备心需要有 担心别人跑路, 价格比较低 严重的是 2000 实际上 你拿到的是200)
        3. 自己发展外包渠道 (最长久/最稳定的渠道)
            技术论坛
            在自媒体平台 发布引流的 视频/文章
            发展自己身边的资源(计算机专业的大学生)
        4. vip会提供专门的外包渠道 (给到你前期学习的时候练手, 拓展渠道用的)
兴趣学 3

爬虫开发
数据分析
网站开发


人工智能: 门槛比较高 对于学历 数学 英语方面 要求比较高

冷门方向
    游戏开发
    桌面应用制作
    自动化运维/测试/办公


就业班:    7个月
    8880 / 24 = 370
兼职班:    5个月
    6680 / 18 = 371.11

时间:
    每周 135 / 246 晚上8-10
    课后 录播+一对一 (直播)
    作业
    冻结学习权限 等自己有时间以后再学
"""
import json
import requests
import re
from tqdm import tqdm

cookies = {
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'RK=41XsVmc90t; ptcz=31e29a7fbc6bd366b8fab54b67e487f1e917f8482f7e3923772d4bbfeb9be737; pgv_pvid=3105898103; fqm_pvqid=5d4f0730-0cc7-4124-9355-dc5de0e7471d; tvfe_boss_uuid=dcf1d31fdfb6fca5; appuser=D4BE6F70A0454042; o_cookie=1321228067; pac_uid=1_1321228067; tmeLoginType=2; euin=oKoAoK-ANens7z**; qq_domain_video_guid_verify=e5c00b680c1444dd; ptui_loginuin=1321228067; lv_play_index=65; o_minduid=X-yJhLPdlUZuCQnlTY0NQvXlfUFPyyav; psrf_qqunionid=FAEE1B5B10434CF5562642FABE749AB9; wxrefresh_token=; wxopenid=; psrf_qqaccess_token=7824EBAD543302363BA502EFB27C0421; psrf_qqopenid=4F37937E43ECA9EAB02F9E89BE1860E2; psrf_qqrefresh_token=A43FCF6790A786722BBF7565F9DBABCF; wxunionid=; ufc=r64_1_1690286676; uin=1321228067; psrf_access_token_expiresAt=1699272502; pgv_info=ssid=s4292370496; vversion_name=8.2.95; video_omgid=e5c00b680c1444dd; LPVLturn=575; LPLFturn=264; LPPBturn=728; LPSJturn=306; LVINturn=265; LPHLSturn=860; LDERturn=505; LZTturn=652; LPDFturn=459',
    'Origin': 'https://v.qq.com',
    'Pragma': 'no-cache',
    'Referer': 'https://v.qq.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# cKey vusession
data = '{"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200h0pywu5%2Fs0046s4mj2v.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200h0pywu5%2Fs0046s4mj2v.html&sphttps=1&encryptVer=9.2&cKey=2ZvwkX252A61Hs1Orq2-LnCjnpb8Ocr0cPTdH03AzEul_f4uOWcpUWJOR8Gr77I5OxAH2x4N0GrkCp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfOXktuBpd_IkL4r7pOA3F3y_IMO54JiFjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWwiX7uSsBkDK_qlv9BvC71CgXl1BaviS_BpuKq82aD5mWuxVCa14y9G6GY7tJ16T3A-rAgvMUdrkyjSUPnwdHttk11GpZzJ9PXhdja1vGklbevt50nAss3hqJ265WoTrXwyJsyx7BWg567fO8YOPujdu8Y2Miop0pceQ9axK4YETxB2VJ4XqYIOYU6KeA-yoIl4rwvkaqxO9bNuP_s5gfOg4smhtpagsXFOwPAivCn4Cj54qIWJb-p93SecJNWQwk3oTXkMu8umUgsGPIo73UjpHLJAgJiBH-b&clip=4&guid=e5c00b680c1444dd&flowid=5b6561d1f8528cde9d5ed24b4b7216b3&platform=10201&sdtfrom=v1010&appVer=1.23.0&unid=&auth_from=&auth_ext=&vid=s0046s4mj2v&defn=uhd&fhdswitch=0&dtype=3&spsrt=2&tm=1692106770&lang_code=0&logintoken=%7B%22access_token%22%3A%223F6CBDF010ACB6A3A3F9C0ACEC7651E6%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22EIF4nFcTMrS1aRoYAGoG-A.N%22%2C%22openid%22%3A%2203A0BB50713BC1C977C0F256056D2E36%22%2C%22vuserid%22%3A%22115600983%22%2C%22video_guid%22%3A%22e5c00b680c1444dd%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&drm=40","sspAdParam":"{\\"ad_scene\\":1,\\"pre_ad_params\\":{\\"ad_scene\\":1,\\"user_type\\":1,\\"video\\":{\\"base\\":{\\"vid\\":\\"s0046s4mj2v\\",\\"cid\\":\\"mzc00200h0pywu5\\"},\\"is_live\\":false,\\"type_id\\":1,\\"referer\\":\\"https://v.qq.com/channel/movie\\",\\"url\\":\\"https://v.qq.com/x/cover/mzc00200h0pywu5/s0046s4mj2v.html\\",\\"flow_id\\":\\"5b6561d1f8528cde9d5ed24b4b7216b3\\",\\"refresh_id\\":\\"e3a997ed98830381698832dd1ddb5ca2_1692101852\\",\\"fmt\\":\\"fhd\\"},\\"platform\\":{\\"guid\\":\\"e5c00b680c1444dd\\",\\"channel_id\\":0,\\"site\\":\\"web\\",\\"platform\\":\\"in\\",\\"from\\":0,\\"device\\":\\"pc\\",\\"play_platform\\":10201,\\"pv_tag\\":\\"www_baidu_com|x\\"},\\"player\\":{\\"version\\":\\"1.22.4\\",\\"plugin\\":\\"3.4.3\\",\\"switch\\":1,\\"play_type\\":\\"0\\",\\"img_type\\":\\"webp\\"},\\"token\\":{\\"type\\":1,\\"vuid\\":115600983,\\"vuser_session\\":\\"EIF4nFcTMrS1aRoYAGoG-A.N\\",\\"app_id\\":\\"101483052\\",\\"open_id\\":\\"03A0BB50713BC1C977C0F256056D2E36\\",\\"access_token\\":\\"3F6CBDF010ACB6A3A3F9C0ACEC7651E6\\"}}}","adparam":"adType=preAd&vid=s0046s4mj2v"}'
# data = '{"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200h0pywu5%2Fs0046s4mj2v.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200h0pywu5%2Fs0046s4mj2v.html&sphttps=1&encryptVer=9.2&cKey=RvCVKuLSvbW1Hs1Orq2-LnCjnpb8Ocr0cPTdH7nqzEul_f4uOWcpUWJOR8Gr77I5OxAH2x4N0GrkCp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfOXktuBpd_IkL4r7pOA3F3y_IMO54JiFjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWwiX7uSsBkDK_qlv9BvC71CgXl1BaviS_BpuKq82aD5mWuxVCa14y9G6GY7tJ16T3A-rAgvMUdrkyjSUPnwdHttk11GpZzJ9PXhdja1vGklbevt50nAss3hqJ265WoTrXwyJsyx7BWg567fO8YOPujdu8Y2Miop0pceQ9axK4YETxB2VJ4XqYIOYU6LOA6m9Zyvr8rk-zkaoDOvP_s5gfOg4smhtpagsXFOwPAivCn4Cj54qIWJb-p93SecJNWQwk3oTWaMSwOAcfp61udoRvEqyUsAgJnXxfV&clip=4&guid=e5c00b680c1444dd&flowid=5b6561d1f8528cde9d5ed24b4b7216b3&platform=10201&sdtfrom=v1010&appVer=1.23.0&unid=&auth_from=&auth_ext=&vid=s0046s4mj2v&defn=uhd&fhdswitch=0&dtype=3&spsrt=2&tm=1692103736&lang_code=0&logintoken=%7B%22access_token%22%3A%223F6CBDF010ACB6A3A3F9C0ACEC7651E6%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22Lry_58Dx2BU-G7A2vMcMPQ.N%22%2C%22openid%22%3A%2203A0BB50713BC1C977C0F256056D2E36%22%2C%22vuserid%22%3A%22115600983%22%2C%22video_guid%22%3A%22e5c00b680c1444dd%22%2C%22main_login%22%3A%22qq%22%7D&spvvpay=1&spadseg=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&drm=40","sspAdParam":"{\\"ad_scene\\":1,\\"pre_ad_params\\":{\\"ad_scene\\":1,\\"user_type\\":1,\\"video\\":{\\"base\\":{\\"vid\\":\\"s0046s4mj2v\\",\\"cid\\":\\"mzc00200h0pywu5\\"},\\"is_live\\":false,\\"type_id\\":1,\\"referer\\":\\"https://v.qq.com/channel/movie\\",\\"url\\":\\"https://v.qq.com/x/cover/mzc00200h0pywu5/s0046s4mj2v.html\\",\\"flow_id\\":\\"5b6561d1f8528cde9d5ed24b4b7216b3\\",\\"refresh_id\\":\\"e3a997ed98830381698832dd1ddb5ca2_1692101852\\",\\"fmt\\":\\"fhd\\"},\\"platform\\":{\\"guid\\":\\"e5c00b680c1444dd\\",\\"channel_id\\":0,\\"site\\":\\"web\\",\\"platform\\":\\"in\\",\\"from\\":0,\\"device\\":\\"pc\\",\\"play_platform\\":10201,\\"pv_tag\\":\\"www_baidu_com|x\\"},\\"player\\":{\\"version\\":\\"1.22.4\\",\\"plugin\\":\\"3.4.3\\",\\"switch\\":1,\\"play_type\\":\\"0\\",\\"img_type\\":\\"webp\\"},\\"token\\":{\\"type\\":1,\\"vuid\\":115600983,\\"vuser_session\\":\\"Lry_58Dx2BU-G7A2vMcMPQ.N\\",\\"app_id\\":\\"101483052\\",\\"open_id\\":\\"03A0BB50713BC1C977C0F256056D2E36\\",\\"access_token\\":\\"3F6CBDF010ACB6A3A3F9C0ACEC7651E6\\"}}}","adparam":"adType=preAd&vid=s0046s4mj2v"}'

response = requests.post('https://vd6.l.qq.com/proxyhttp', cookies=cookies, headers=headers, data=data)
# 2. 取到整个数据
vinfo = response.json()['vinfo']
# 3. 将需要的.m3u8链接提取出来
# 3.1 将 vinfo (json字符串) 转为 字典数据
json_data = json.loads(vinfo)
# print(json_data)
# m3u8 -> ul -> 0 -> vi -> vl
m3u8_text = json_data['vl']['vi'][0]['ul']['m3u8']
# 4. 将其中的 所有的ts片段视频链接 取到
# 4.1 将所有 #E 开头的内容 匹配 并去掉 是不是就可以得到 所有的ts
m3u8_text = re.sub('#E.*', '', m3u8_text)
# 4.2 将 m3u8_text 进行切割 对空白内容切割 切割之后可以得到一个 ts的列表
ts_list = m3u8_text.split()
# 5. 将每个ts片段链接拼接好
for ts in tqdm(ts_list):
    ts_url = 'https://ltsgdty.gtimg.com/B_RXEIgyrEeptqIGFsNBAPyuefDiV-tinQxrMYAbrPW8171s8vsKbhTI95DsxGiJ76/zkK8j1qI-4rzjf52zUQSMe0rrXN8J6YE1xW4RNgy6bGtYSYUB82h72i_-gTJVxqju3iQ3JqgCH2ymY6U17rNayLeUkv6ewqnUOa7sGySrm6oDnpRyhn1Hshm-pg8hruIKHLOrSj01JJVoMVQG8TdA7GdqLBu3WGgZhs8SCB8vzoM2IAYdj_aJxYQaxeVAjcL/' + ts
    # 6. 挨个访问 并保存为一个视频
    ts_data = requests.get(ts_url).content
    open('兴安岭猎人传说2轮回森林.mp4', mode='ab').write(ts_data)
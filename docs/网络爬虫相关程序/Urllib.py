# import urllib.request
# import urllib.parse
# import json
#
# url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
#
# headers = {
#     # 'Accept': ' */*',
#     # 'Accept-Encoding': ' gzip, deflate, br',# “Accept—Encoding”代表接受的代码形式，注释掉
#     # 'Accept-Language': ' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     # 'Acs-Token': ' 1692612127850_1692612133261_wH/dU2+u9QSAbp4C5NstSDnmmnbA6zgsKlESxaEQ/IoIPMfYfHrYv0aqILeKI9Mzu+L1pMJQZEbP47lDkx/hqsfxvI7DcNy1OLuqRwbCC6suuEXon5HqPu669GAar6LtLq3dIJri32otTE0ovEms+aP8CrTskQRFuhIJNp7rXF75p2amoDvqnerHIegLJs5bumazqNmHGaowLfA6t93XEjQIelXztw6X4KJJe6VwGU+6h6RVDNGa1MBOidg2DiEN7mQ1DH0aGDvquvMO3DidvaEs3z2TS/Dg0Jgt7gBbztPxbqb4Ly+Vn72VnQp7uP9+nfUhWH3MUL8Vmj3BXABX+VoWtkPK+F/i92KXas009+BBj2rmm/nMXiTQNhMumn+jDPzslimG7fDt5WNTLye5pYDPXjixGbkEQ7WWO+5O9GJLlUV6jE7Vc9r4EpSN1Ef/7p+kp0GW7KwMDYoxVS+DjqcpsJmGIasTVLvO2JCNhqM=',
#     # 'Connection': ' keep-alive',
#     # 'Content-Length': ' 152',
#     # 'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie': 'BIDUPSID=C0ACBBBACB079AEA6E144A1188972DD3; PSTM=1657006868; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; H_WISE_SIDS_BFESS=107313_110085_179346_180636_194519_196427_197711_199578_204916_206123_208721_209202_209568_210305_210321_212296_212740_213041_213306_213347_214115_214130_214137_214143_214807_215107_215727_216207_216651_216847_216883_216942_217167_218350_218359_218445_218548_218567_218597_218620_219244_219363_219413_219452_219566_219592_219666_219733_219742_219842_219908_219942_219946_220071_220090_220301_220392_220394_220603_220662_221040_221091_221108_221116_221118_221121_221303_221369_221381_221474_221624_221717_221953_222135; BAIDUID_BFESS=C0ACBBBACB079AEA6E144A1188972DD3:FG=1; __bid_n=1841714890f98900514207; FEID=v10-e7bbcfc5c364bf675f7626b26958c26ed9b32ad6; __xaf_fpstarttimer__=1672411900204; __xaf_thstime__=1672411900220; __xaf_fptokentimer__=1672411900639; BAIDU_WISE_UID=wapp_1678099817097_320; FPTOKEN=3k09SxYXZHEWUrcwLA0gaIuQ8jzx46+kcmPNFq2Gnsli9j4eEPnMeQxHKG0a6aXLeA0dy+twOkoG/X7t0xCZhzvTFw3DiWKD1K4lpZ/hFdGkjEd5bvl3iZBqw8ZxI5Lp7GJe9HfQ682Mt/IAZ19ajFG7Qc32brPSHUG6hsr3rExw86mlvAsZVomQrEWfzLWNAV3MvJ9YDiIp4R015XJ4nVH+z6FhH6GKe9pqnnIY564dj4ZiB+M7kkAYf+p3yaljzokYW1q2b4lYDxFT3mevfV6X1QY1DEBXF9tIGnLwmz0IT1XAhVeDviIeDa7obwnpTgWS9uPZkzo/qkhJjLpkBF2ua2xoYyaEYr21vJ2S8JJP8zQelX8UzF4CXOWo33X289y3q/uPqwtrsZpjPIep/w==|Y57w4GO9ZEEzzvBRF1XxfkMfj8zwR+6aMfznMANKDi0=|10|840a51e403a2341e47257767c2107062; BDUSS=mJkbnNuTEt0UjYxdEF0QnNhdkFLOWVJNXBmWmRVUVdQTGJTb3JRdVJSbEp5ZnBrRVFBQUFBJCQAAAAAAAAAAAEAAADvAF1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEk802RJPNNkW; BDUSS_BFESS=mJkbnNuTEt0UjYxdEF0QnNhdkFLOWVJNXBmWmRVUVdQTGJTb3JRdVJSbEp5ZnBrRVFBQUFBJCQAAAAAAAAAAAEAAADvAF1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEk802RJPNNkW; newlogin=1; SEARCH_MARKET_URL=http%3A//wenku.baidu.com/ndlaunch/browse/view/a36543b4142ded630b1c59eef8c75fbfc67d9453%3Ffr%3Dlaunch_ad%26SS-bdtg52%3D%26utm_source%3Dbdss-WD%26utm_medium%3Dcpc%26keyword%3D%25E5%2590%2584%25E4%25B8%25AA%25E5%25A4%25A7%25E5%25AD%25A6%25E7%259A%2584%25E4%25BB%25A3%25E7%25A0%2581%26utm_account%3DSS-bdtg52%26utm_term%3D2%26utm_content%3D2%26e_creative%3D56770332540%26e_keywordid%3D370002894972%26bd_vid%3D11153425114272312900; ab_sr=1.0.1_YTJjOGY4NzZhMjZjMGFiMDNkMjBmOGMzMTAzMjZhMWI4ZmI5YjQ3ZTU3NmFjNzliZGVkY2FkYzQ4ZTFiMTU5NGQ3Zjg1MzA1YmYyYTAwMGQ5N2RmOWI1NDkwNjBjNjRhYTIzZGRjZjMxMjAxOGI1NmMzMTUxMzc2NjA0NzNlNDQwYTQxN2M1YmQyZjkwNzU5OTM4MTEyMzNjZGNiZDY0ZjE3NDhhZmFkNTdmYTE5NTM1MWViMWUwYzgxZjAwMjY2',
#     # 'Referer': 'https://fanyi.baidu.com/',
#     # 'Sec-Fetch-Dest': 'empty',
#     # 'Sec-Fetch-Mode': 'cors',
#     # 'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
#     # 'X-Requested-With': 'XMLHttpRequest',
#     # 'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
#     # 'sec-ch-ua-mobile': '?0',
#     # 'sec-ch-ua-platform': '"Windows"',
# }
#
# data = {
#     'from': 'en',
#     'to': 'zh',
#     'query': 'love',
#     'transtype': 'realtime',
#     'simple_means_flag': '3',
#     'sign': '198772.518981',
#     'token': 'ae392291932a0dbf0062dcdeb46b71cb',
#     'domain': 'common',
#     'ts': '1692614132997',
# }
#
# # post请求的参数 必须进行编码  并且要调用encode方法
# data = urllib.parse.urlencode(data).encode("utf-8")
#
# # 请求对象的定制
# request = urllib.request.Request(url=url, data=data, headers=headers)
#
# # 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
#
# # 获取响应的内容
# content = response.read().decode('utf-8')
#
#
# obj = json.loads(content)
# print(obj)


# import urllib.request
# import urllib.parse
# import json
#
# url = "https://fanyi.baidu.com/sug"
#
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
# }
#
# data ={
#     "kw": "spider"
# }
#
# #post请求的参数  必须进行编码
# data = urllib.parse.urlencode(data).encode("utf-8")
#
# #post请求的参数  是不会拼接在url的后面的 而是需要放在请求对象定制的参数中
# #post请求的参数  必须进行编码
# request = urllib.request.Request(url=url,data=data,headers=headers)
# print(request)
#
# # 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
#
# # 获取响应的内容
# content = response.read().decode('utf-8')
#
# #字符串———>json对象
# obj = json.loads(content)
# print(obj)
#
# #post请求方式的参数  必须编码  data = urllib.parse.urlencode(data)
# #编码之后 必须调用encode方式   data = urllib.parse.urlencode(data).encode("utf-8")
# #参数的放在请求对象定制的方法中  request = urllib.request.Request(url=url,data=data,headers=headers)


# import urllib.request
# import urllib.parse
#
# base_url = "https://www.baidu.com/s?"
# data = {
# 	"wd":"周杰伦",
# 	"sex":"男",
# 	"location":"中国台湾省",
# }
#
# new_data = urllib.parse.urlencode(data)
#
# #请求资源路径
# url = base_url + new_data
#
# #请求对象的定制为了解决反爬的第一种手段
# headers={
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
# }
#
# #请求对象的定制
# request = urllib.request.Request(url=url,headers=headers)
#
# #模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
#
# #获取响应的内容
# content = response.read().decode('utf-8')
#
# #打印数据
# print(content)


# get请求
# 获取豆瓣电影的第一页的数据  并且保存起来
# import urllib.request
#
# url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
# }
#
# #(1)请求对象的定制
# request = urllib.request.Request(url=url,headers=headers)
#
# #(2)获取响应数据
# #模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
#
# #获取响应的内容
# content = response.read().decode('utf-8')
#
# #(3)数据下载到本地
# #open方法默认情况下使用的是gbk的编码  如果我们要想保存汉字 那么需要open方法中指定编码格式为utf-8
# #encoding=“utf-8”
#
# with open('douban.json','w', encoding='utf-8') as f:
#     f.write(content)


# # 获取豆瓣电影前十页内容
#
# import urllib.parse
# import urllib.request
#
#
# def create_request(page):
#     base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&"
#
#     data = {
#         'start': (page - 1) * 20,
#         'limit': 20
#     }
#
#     data = urllib.parse.urlencode(data)
#
#     url = base_url + data
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
#     }
#
#     request = urllib.request.Request(url=url, headers=headers)
#
#     return request
#
#
# def get_content(request):
#     response = urllib.request.urlopen(request)
#     content = response.read().decode("utf-8")
#     return content
#
#
# def down_load(page, content):
#     with open("douban" + str(page) + ".json", "w", encoding='utf-8') as f:
#         f.write(content)
#
#
# # 程序入口
# if __name__ == '__main__':
#     start_page = int(input('请输入起始页码'))
#     end_page = int(input('请输入结束页码'))
#
#     for page in range(start_page, end_page+1):
#         #   每一页都有自己的请求对象的定制
#         request = create_request(page)
#         #   获取响应数据
#         content = get_content(request)
#         #   下载
#         down_load(page, content)


# import urllib.request
# import urllib.parse
#
#
# def create_request(page):
#     base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
#
#     data = {
#         "cname": "北京",
#         "pid": "",
#         "pageIndex": page,
#         "pageSize": "10",
#     }
#
#     data = urllib.parse.urlencode(data).encode("utf-8")
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
#     }
#     request = urllib.request.Request(url=base_url, headers=headers, data=data)
#
#     return request
#
#
# def get_content(request):
#     response = urllib.request.urlopen(request)
#     content = response.read().decode("utf-8")
#     return content
#
#
# def down_load(page,content):
#     with open('kfc_' + str(page) + '.json', "w", encoding="utf-8")as f:
#         f.write(content)
#
#
# if __name__ == "__main__":
#     start_page = int(input("请输入起始页码"))
#     end_page = int(input("请输入结束页码"))
#
#     for page in range(start_page, end_page + 1):
#         # 请求对象的定制
#         request = create_request(page)
#         # 获取网页源码
#         content = get_content(request)
#         # 下载
#         down_load(page,content)

# import  urllib.request
# import  urllib.error
#
# url = "https://blog.csdn.net/csdnnews/article/details/1324193141"
#
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
# }
#
# try:
#     request = urllib.request.Request(url=url,headers=headers)
#
#     response = urllib.request.urlopen(request)
#
#     content = response.read().decode("utf-8")
#     print(content)
#
# except urllib.error.HTTPError:
#     print("系统正在升级中。。。")
#
# except urllib.error.URLError:
#     print("系统正在升级中。。。")


# 适用场景：数据采集的时候 需要绕过登录 然后进入到某个页面
# 个人信息页面是utf-8 但是还报错了代码错误  因为并没有进入到个人信息页面 而是跳转到了登录页面
# 那么登录页面不是utf-8 所以报错

# 什么情况下访问不成功？
# 因为请求头都信息不组  所以访问不成功

# import urllib.request
#
# url = "https://weibo.cn/"
#
# headers = {
#     # ':authority': 'weibo.cn',
#     # ':method': 'GET',
#     # ':path': '/7781529952/info',
#     # ':scheme': 'https',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'Cache-Control': 'max-age=0',
#     #cookie中携带着你的登录信息  如果有登录之后的cookie 那么我们可以携带cookie进入到任何界面
#     'Cookie': 'SCF=AjyMMDsVFp3jQnKKLRuY8unKmhdMku6pN3CdsGmjG_IsDUbabBfKASzWTDJZfLO4Etpj2M67BegQhzTB8JfwcHA.; SUB=_2A25J4B49DeRhGeFJ41MU8ifFzj6IHXVrKqJ1rDV6PUJbktAGLWekkW1Nfx81xo-tSBthxQqzGVlR6OXmGhAqxGjO; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhvPoXPKLFOSiT.BXXhs_pT5JpX5K-hUgL.FoMN1h2feo.4SKz2dJLoIpSAi--ciKnRiK.7i--fiKy2iK.0; SSOLoginState=1692692078; ALF=1695284078; _T_WM=0fd99d891b110cc038949897c7e0d84b',
#     #referer是做防盗链的，判断当前路径是不是由上一个路径进来的  一般情况下 是做图片防盗链
#     'Referer': 'https://weibo.cn/',
#     'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Windows"',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
# }
# # 请求对象的定制
# request = urllib.request.Request(url=url, headers=headers)
# # 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(request)
# # 获取响应的数据
# content = response.read().decode("utf-8")
#
# # 将数据保存到本地
# with open('weibo.html', 'w', encoding='utf-8')as fp:
#     fp.write(content)


# #需要 使用handler来访问百度 获取网页源码
#
# import urllib.request
#
# url = "http://baidu.com"
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
# }
#
# request = urllib.request.Request(url=url,headers=headers)
#
# #handler  bulid_opener open
#
# #(1)获取handler对象
# handler = urllib.request.HTTPHandler()
#
# #(2)获取opener对象
# opener = urllib.request.build_opener(handler)
#
# #(3)调用open方法
# response = opener.open(request)
#
# content = response.read().decode("utf-8")
#
# print(content)


# import urllib.request
#
# url = "https://www.baidu.com/s?wd=ip"
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
# }
#
# # 请求对象的定制
# request = urllib.request.Request(url=url, headers=headers)
#
# # #模拟浏览器访问服务器
# # response = urllib.request.urlopen(request)
#
# proxies = {
#     'http': '127.0.0.1:7890',
#     'https': '127.0.0.1:7890',
# }
#
# # handler  bulid_opener open
#
# # (1)获取handler对象
# handler = urllib.request.ProxyHandler(proxies=proxies)
#
# # (2)获取opener对象
# opener = urllib.request.build_opener(handler)
#
# # (3)调用open方法
# response = opener.open(request)
#
# # 获取响应的信息
#
# content = response.read().decode("utf-8")
#
# # 保存
# with open("daili.html", "w", encoding="utf-8") as fp:
#     fp.write(content)


# proxies_pool=[
#     {'http':'118.24.219.151:16817'},
#     {'http':'127.0.0.1:7890'}
# ]
#
# import random
#
# proxies=random.choice(proxies_pool)
#
# print(proxies)

# curl cip.cc


# import urllib.request
# from lxml import etree
# url = "http://www.baidu.com/"
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
# }
#
# # 请求对象的定制
# request = urllib.request.Request(url=url, headers=headers)
#
# #模拟浏览器访问服务器
# response = urllib.request.urlopen(request)
#
# #获取网页源码
# content = response.read().decode("utf-8")
#
# #解析网页源码 来获取我们想要的数据
# #解析服务器响应的文件
# tree=etree.HTML(content)
#
# #获取想要的数据   xpath的返回值是一个列表类型的数据 加[0]得到第一个元素其类型为字符串
# result = tree.xpath('//input[@id="su"]/@value')[0]
# print(result)


# （1）请求对象的定制
# （2）获取网页源码
# （3）下载


# 需要 下载的前十页的照片
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html

import urllib.request
from lxml import etree


def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    }

    # 请求对象的定制
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(content):
    #    下载图片
    #     urllib.request.urlretrieve("图片地址","文件的名字")
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@data-marginr="16"]//div/img/@alt')

    # 一般设计到图片的网站都会涉及到懒加载，不取便之后的，取变之前的路径。
    src_list = tree.xpath('//div[@data-marginr="16"]//div/img/@data-original')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='./图片/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page + 1):
        # (1)请求对象的定制
        request = create_request(page)
        # (2)获取网页的源码
        content = get_content(request)
        # (3)下载
        down_load(content)

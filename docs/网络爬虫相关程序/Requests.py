# import requests
#
# url = "http://www.baidu.com"
#
# response = requests.get(url=url)
#
# #一个类型和六个属性
#
# #Response类型
# # print(type(response))
#
# #设置响应的编码格式
# response.encoding="utf-8"
#
# #以字符串的形式来返回网页中的源码
# print(response.text)
#
# #返回一个url地址
# print(response.url)
#
# #返回的是二进制的数据
# print(response.content)
#
# #返回响应的状态码
# print(response.status_code)
#
# #返回的是响应头
# print(response.headers)


# import requests
#
# url = "https://www.baidu.com/s?"
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
# }
# data = {
#     'wd':'北京'
# }
#
# # url 请求资源路径
# # params 参数
# # kwargs 字典
#
# response = requests.get(url=url, params=data, headers=headers)
# response.encoding="utf-8"
#
# content = response.text
#
# print(content)
#
# #总结
# #参数使用params传递
# #参数无需urlencode编码
# #不需要请求对象的定制
# #定制资源路径中的?可以加也可以不加


# import requests
#
# url = 'https://fanyi.baidu.com/sug'
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
# }
#
# data={
#     'kw':'eye'
# }
#
# #url 请求地址
# #data 请求参数
# #kwargs 字典
# response = requests.post(url=url,data=data,headers=headers)
#
# content =response.text
#
# import json
# obj = json.loads(content,encoding="utf-8")
# print(obj)
#
# #总结
# #(1)post请求 是不需要编解码
# #(2)post请求的参数是data
# #(3)不需要请求对象的定制

# import requests
#
# url = "https://ip.900cha.com/"
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
# }
#
# proxy={
#     'https':'127.0.0.1:7890',
# }
#
# response=requests.get(url=url,headers=headers,proxies=proxy)
#
# content = response.text
#
# with open('daili.html','w',encoding='utf-8')as fp:
#     fp.write(content)







# 通过登录  然后进入到主页面


# 通过找登录的接口我们发现  登陆的时候需要的参数很多
# __VIEWSTATE: DwkGU98uLnbkaMO7skba8X2aS34NidLfa8MMtLf+IFQZ2BXUCPMfshHjZLztJQlr3AWAAt4m18Ode+ooTPLCpYOE/devXsNdHfBp0XSVWJrKVxWnrxmRY/E86kA2msl5oCLQT6pzReKmUgnzvp5/4js1pV4=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 2973371334@qq.com
# pwd: Zcz@1234
# code: 9D73
# denglu: 登录

# 我们观察到__VIEWSTATE  __VIEWSTATEGENERATOR  code是一个可以变化的量

# 难点:(1)__VIEWSTATE  __VIEWSTATEGENERATOR 一般情况看不到数据 都在原页面的源码中
#     我们观察到这个数据在页面的源码中  所以我们需要获取页面的源码 然后进行解析就可以获取了
#     (2)验证码

# import requests
#
# # 这个是登陆页面的url地址
# url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54',
# }
#
# # 获取页面的源码
# response = requests.get(url=url, headers=headers)
# content = response.text
# # 解析页面源码  然后获取__VIEWSTATE  __VIEWSTATEGENERATOR
# from lxml import etree
#
# html_tree = etree.HTML(content)
# # 获取__VIEWSTATE
# viewstate = html_tree.xpath('//input[@id="__VIEWSTATE"]/@value')
# print(viewstate)
# # 获取__VIEWSTATEGENERATOR
# viewstategenerator = html_tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')
# print(viewstategenerator)
# # 获取验证码图片
# code = html_tree.xpath('//img[@id="imgCode"]/@src')
# code_url = 'http://so.gushiwen.cn' + code[0]
# # 有坑
# # import urllib.request
# # urllib.request.urlretrieve(url=code_url,filename='code.jpg')
# # requests里面有一个方法 session() 通过session的返回值 就能使用请求变成一个对象
#
#
# session = requests.session()
# # 验证码的url的内容
# response_code = session.get(code_url)
# # 注意此时要使用二进制数据写入到文件
# content_code = response_code.content
# # wb的模式就是将二进制数据写入到文件
# with open('code.jpg', 'wb')as fp:#wb写入二进制数据： 你可以将二进制数据写入文件，比如图片、音频、视频等
#     fp.write(content_code)
#
# # 获取了验证码的图片之后 下载到本地 然后观察验证码 观察之后 然后在控制台输入这个验证码 就可以将这个值给code的参数 就可以登录
#
# code_name = input('请输入验证码')
#
# # 点击登录
# url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
#
# data_post = {
#     '__VIEWSTATE': viewstate,
#     '__VIEWSTATEGENERATOR': viewstategenerator,
#     'from: http': '//so.gushiwen.cn/user/collect.aspx',
#     'email': '2973371334@qq.com',
#     'pwd': 'Zcz@1234',
#     'code': code_name,
#     'denglu': '登录',
# }
#
# response_post = session.post(url=url, headers=headers, data=data_post)
#
# content_post = response_post.text
#
# with open('gushuiwen.html', 'w', encoding='utf-8')as fp:
#     fp.write(content_post)
#
# # 难点
# # (1)隐藏域
# # (2)验证码

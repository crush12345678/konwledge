* **Xpath**

  > 1.解析本地文件【etree.parse()】：
  >
  > ​	html_tree=etree.parse('xx.html')
  >
  > 2.解析服务器响应文件【etree.HTML()】
  >
  > ​	html_tree = etree.HTML(response.read().decode("utf-8"))

* **获取百度网站的百度一下**

  * ~~~python
    import urllib.request
    from lxml import etree
    url = "http://www.baidu.com/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    }
    
    # 请求对象的定制
    request = urllib.request.Request(url=url, headers=headers)
    
    #模拟浏览器访问服务器
    response = urllib.request.urlopen(request)
    
    #获取网页源码
    content = response.read().decode("utf-8")
    
    #解析网页源码 来获取我们想要的数据
    #解析服务器响应的文件
    tree=etree.HTML(content)
    
    #获取想要的数据   xpath的返回值是一个列表类型的数据 加[0]得到第一个元素其类型为字符串
    result = tree.xpath('//input[@id="su"]/@value')[0]
    print(result)
    ~~~

* **获取图片**

  * ~~~python
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
    ~~~


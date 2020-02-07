import urllib.request
import urllib.parse
import re
from datetime import datetime

import auto_email


class Spider:
    """
    创建Spider爬虫类，其中包括以下方法：
    """

    def __init__(self, url, header, formdata, proxy):
        """
        :param url: 目标爬取的地址，可使用Fiddler辅助获取网站请求数据时的URL
        :param header: 伪装浏览器的头部信息。最主要的是要有user-agent，其他数据根据网站要求酌情决定，不确定时可逐行注释，然后运行尝试。
        :param formdata: 表单数据内容。当提交POST请求时，所有提交给网站的表单数据均放在这个字典里。
        :param proxy: 使用代理IP访问网站，能避免一些普通的网站封号情况的发生（尤其是频繁请求时）。
        """
        self.url = url
        self.header = header
        self.formdata = formdata
        self.proxy = proxy

    def send_request(self):
        """
        1.访问网页，发送请求
        """
        # 通过urllib.parse拼接url+参数=完整URL（可以打印一下，查看是否与浏览器request header中的请求地址一样）
        formdata = urllib.parse.urlencode(self.formdata).encode()

        # 使用IP proxy
        """
        1.设置代理IP以及端口
        2.创建Proxyhandler
        3.创建opener
        4.安装opener
        """
        proxy_obj = urllib.request.ProxyHandler(proxies=self.proxy)
        opener = urllib.request.build_opener(proxy_obj)
        urllib.request.install_opener(opener)

        # 发送Request（包含URL和header）
        request = urllib.request.Request(self.url, headers=self.header)

        # 发送URLopen（包含Request和formdata）
        self.response = urllib.request.urlopen(url=request, data=formdata)
        self.excute_response()

    def excute_response(self):
        """
        2.接收数据，并根据对方的格式进行清洗（可选择正则表达式、Jsonpath等语言）
        """
        # 通过正则处理过后的返回结果（类型：列表）
        self.result_title = re.findall(r'title":"(.*?)",', self.response.read().decode())
        self.file_save()

    def file_save(self):
        """
        3.写入文件
        """
        print("开始执行IO方法")
        try:
            fp = open(r"爬取结果.txt", "w")
            fp.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            for item in self.result_title:
                fp.write(item + "\n")
            print("数据写入成功")
            fp = open(r"爬取结果.txt")
            content = fp.read()
            self.user_controller(content)
            fp.close()
        except FileNotFoundError:
            with open(r"爬取结果.txt", "w") as fp:
                print("文件创建成功")

    def user_controller(self, content):
        """
        4.用户控制器（非必须，在数据爬取成功之后向用户发送邮件）
        """
        # 读取爬虫结果文件，并且执行发送邮件方法
        print("文件已打开")
        auto_email.Send_email(recei_list, email_title, content)


"""
以下为执行爬虫方法所需的参数
"""
# 定义URL（请注意带上url最后面的问号，URL中的参数或者表单中的参数都在formdata里面填写。然后urllib提供了parse会自动编译且生成完整的请求URL（和在浏览器地址栏中见到的一样）
url = "XXX"

# 伪装header
header = {
    # 伪装成浏览器，最主要的是要有user-agent。其他数据根据网站要求酌情决定，不确定时可逐行注释，然后运行尝试。
}

# 解析formdata并进行编译（可通过fiddler软件辅助查看请求的时候都向目标网站传递了哪些参数）
formdata = {

}

# 通过代理IP和端口访问，以避免在频繁使用同一IP访问时被对方封掉。
# 可访问代理IP提供网站 https://www.xicidaili.com/nn/ 获得IP和端口
proxy = {
    "http": "60.167.20.200:38786"
}

"""
以下为执行发送邮件方法所需的参数
"""
recei_list = ["xxx"]  # 将接受方的邮箱地址存在一个列表里面
email_title = "XXXXX"  # 邮件标题

# 创建一个爬虫实例对象，以供主函数调用
spider_tecent_news = Spider(url, header, formdata, proxy)

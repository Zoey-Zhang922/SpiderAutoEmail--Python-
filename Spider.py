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
url = "https://pacaio.match.qq.com/irs/rcd?"

# 伪装header
header = {
    "accept-language": "en, en - US;q = 0.9, zh - CN;q = 0.8, zh;q = 0.7",
    "cookie": "tvfe_boss_uuid = 8def89799ee6e2e3;pgv_pvid = 2262001280;pac_uid = 0_5dc81b3d0e7e1;pgv_pvi = "
              "3285164032;RK = XK7EpJdYPj;ptcz = "
              "3ff8692644e238f507420b2b5479e476dd7e4ad1f6ffda16a74647bcc0f52e10;pgv_info = ssid = "
              "s133614294;ts_uid = 2404414514;ts_last = new.qq.com / ch / world /;ad_play_index = 85",
    "user-agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / "
                  "79.0.3945.88Safari / 537.36",
}

# 解析formdata并进行编译
formdata = {
    "cid": "135",
    "token": "6e92c215fb08afa901ac31eca115a34f",
    "ext": "world",
    "page": "1",
    "expIds": "20200131009129|20200203A049ND|20200203A04L93|20200203A0271M|20200203A009T6",
    "expIds": "20200201A04Q9M|20200201A0CE83|20200201A0HESF|20200201A0FRVA|20200201A09EEK|20200201V06Y9D"
              "|20200201A04I6R|20200121A0ME7R|20200201V05BCV|20200201A0HESC",
    "callback": "__jp9"
}

# 通过代理IP和端口访问，以避免在频繁使用同一IP访问时被对方封掉。
# 可访问代理IP提供网站 https://www.xicidaili.com/nn/ 获得IP和端口
proxy = {
    "http": "60.167.20.200:38786"
}

"""
以下为执行发送邮件方法所需的参数
"""
recei_list = ["zhangzeyu922@yeah.net"]
email_title = "每日国际新闻晚报"

# 创建一个爬虫实例对象，以供主函数调用
spider_tecent_news = Spider(url, header, formdata, proxy)

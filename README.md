# SpiderAutoEmail———使用Python3语言
一个基础的Python爬虫项目：自动定时爬取特定网站数据，并发送邮件至用户。主要涉及Python基础知识以及HTTP请求，暂未使用多线程等方式管理性能，后期不断更新。

## 准备工作
### 系统环境
Windows/Mac/Linux</br>
Python环境（安装教程自行谷歌）</br>
Chrome/FireFox浏览器
### 目标网站
假设我们要爬取腾讯国际新闻：https://new.qq.com/ch/world/</br>
打开网页之后，右键审查元素-->网络-->找到请求的URL-->Headers-->Request URL
### 辅助软件
如果你对如何获取到网页请求的url还不是很熟悉，在Windows环境下可以通过使用抓包工具fiddler帮助你轻松地解决这个问题。这里就不再过多的赘述fiddler如何使用，具体的自行谷歌一下，很简单实用。</br>
</br>
## 运行步骤
### 1.在代码中填写必要的信息，包括以下参数（源码已经经过脱敏处理）
main.py Line21</br>
trigger = "" 定义使用何种定时方式，具体值可以搜索BlockingScheduler()类的定义。我这里写的是cron，代表每周几到周几的几点几分循环执行程序。你也可以设置成某一天的几点定时执行程序。</br>
day_of_week='1-5' 每周一至周五</br>
hour=20 晚上八点</br>
minute=8 八分整</br>
</br>
Spider.py Line91</br>
url = "XXX" 定义URL（请注意带上url最后面的问号，URL中的参数或者表单中的参数都在formdata里面填写。然后urllib提供了parse会自动编译且生成完整的请求URL（和在浏览器地址栏中见到的一样</br>
</br>
Spider.py Line94</br>
header = {} 伪装成浏览器，最主要的是要有user-agent。其他数据根据网站要求酌情决定，不确定时可逐行注释，然后运行尝试。</br>
</br>
Spider.py Line99</br>
formdata = {} 解析formdata并进行编译（可通过fiddler软件辅助查看请求的时候都向目标网站传递了哪些参数）</br>
</br>
Spider.py Line105</br>
proxy = {
    "http": "60.167.20.200:38786"
} 通过代理IP和端口访问，以避免在频繁使用同一IP访问时被对方封掉。可访问代理IP提供网站 https://www.xicidaili.com/nn/ 获得IP和端口</br>
</br>
Spider.py Line112</br>
recei_list = ["xxx"]  将接受方的邮箱地址存在一个列表里面
</br>
Spider.py Line113</br>
email_title = "XXXXX" 邮件标题
</br>
auto_email.py Line23</br>
"from": "XXX" 自己的邮箱账号，将使用此账号向对方发送邮件</br>
</br>
auto_email.py Line25</br>
"hostname": "smtp.qq.com" 邮件代理商smtp的地址
</br>
auto_email.py Line26</br>
"username": "XXX" 准备一个开通smtp服务的邮箱账号用来发邮件
</br>
auto_email.py Line27</br>
"password": "XXX" 开通smtp服务的邮箱授权码，每个邮件代理商规则不同，自行百度（主流有QQ，网易）
</br>
auto_email.py Line32</br>
server = smtplib.SMTP_SSL(mail_info["hostname"], port=465)  端口号可在邮件代理商的官网查看
</br>
### 2.运行main.py
方式一：</br>命令行输入 ：python+要运行的python文件绝对路径</br>
比如python C:\Users\Chris Manny\Desktop\Spider&auto-email\main.py</br>
方式二：</br>
使用pycharm或者其他编译器打开项目，运行main.py文件


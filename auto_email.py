# -*- coding: utf-8 -*-

'''
@Time    : 2020/2/5 21:28
@Author  : Zoey Zhang
@FileName: auto_email.py
@Software: PyCharm
 
'''

import smtplib
import email
from email.mime import multipart  # import MIMEMultipart
from email.mime import text  # import MIMEText


# 邮箱认证
# "username": "***@***.com",
# "password": "******",
def Send_email(recei_list, email_title, email_content):
    print("----------准备发送邮件----------")
    mail_info = {
        "from": "XXX",  # 自己的邮箱账号，将使用此账号向对方发送邮件
        "to": recei_list,  # 接收邮件的对方账号
        "hostname": "smtp.qq.com",  # 邮件代理商smtp的地址
        "username": "XXX",  # 开通smtp服务的邮箱账号
        "password": "XXX",  # 开通smtp服务的邮箱授权码，每个邮件代理商规则不同，自行百度（主流有QQ，网易）
        "mail_encoding": "utf-8"
    }

    try:
        server = smtplib.SMTP_SSL(mail_info["hostname"], port=465)  # 端口号可在邮件代理商的官网查看
        server.ehlo(mail_info["hostname"])
        server.login(mail_info["username"], mail_info["password"])  # 仅smtp服务器需要验证时
        print("成功登录邮箱服务器")

        # 构造MIMEMultipart对象做为根容器
        main_msg = multipart.MIMEMultipart()
        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = text.MIMEText(email_content, _charset="utf-8")
        main_msg.attach(text_msg)
        print("邮件内容写入成功")

        # 设置根容器属性
        main_msg['From'] = mail_info['from']
        main_msg['To'] = ';'.join(recei_list)
        main_msg['Subject'] = email_title
        main_msg['Date'] = email.utils.formatdate()

        # 得到格式化后的完整文本
        fullText = main_msg.as_string()

        # 用smtp发送邮件
        try:
            server.sendmail(mail_info['from'], recei_list, fullText)
            print("发送成功")
        except smtplib.SMTPException as e:
            print(e)
            print("最后发送时出现了问题...")
        finally:
            server.quit()

    except smtplib.SMTPException as e:
        print(e)

    """
    如果需要上传附件，则使用以下代码
    """
    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    # for file_name in file_name_list:
    #     ## 读入文件内容并格式化 [方式1]
    #     data = open(file_name, 'rb')
    #     ctype, encoding = mimetypes.guess_type(file_name)
    #     if ctype is None or encoding is not None:
    #         ctype = 'application/octet-stream'
    #     maintype, subtype = ctype.split('/', 1)
    #     file_msg = base.MIMEBase(maintype, subtype)
    #     file_msg.set_payload(data.read())
    #     data.close()
    #     email.encoders.encode_base64(file_msg)  # 把附件编码
    #
    #     ## 设置附件头
    #     basename = os.path.basename(file_name)
    #     file_msg.add_header('Content-Disposition', 'attachment', filename=basename, encoding='utf-8')
    #     main_msg.attach(file_msg)

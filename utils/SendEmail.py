from typing import List
from models import Config, EmailTemplate, EmailAll, ConfigAll


# content = """
#     这是内容
# """
#
# msg = MIMEText(content, 'plain', 'utf-8')
#
# msg['From'] = 'gxlove_max@163.com'
# msg['To'] = '2016415409@qq.com'
# msg['cc'] = ''
# msg['Subject'] = '测试'
#
# # 发送邮件
# smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
# smtp.login('gxlove_max@163.com', 'BPJNGKUTUOIXZZGD')
# smtp.sendmail('gxlove_max@163.com', ['2016415409@qq.com'], msg.as_string())
# smtp.quit()

class SendEmail(object):
    def __init__(self,
                 ToMail: List,
                 MailType: str = '163' or 'qq',
                 ToRole: str = 'blogger-default' or 'user-default' or 'vcode-default'):
        self.MailType = MailType
        self.ToRole = ToRole
        self.ToMail = ToMail
        self.MailConfig: ConfigAll = None
        self.MailTel: EmailAll = None
        self.config = None
        self.Template = None

    async def init_config(self):
        self.MailConfig = await Config.filter(name="email").first()
        self.MailTel = await EmailTemplate.filter(name=self.ToRole).first()
        self.config = self.MailConfig.value['type'][self.MailType]
        self.Template = self.MailTel.code

    def _content(self, **kwargs):
        from email.mime.text import MIMEText
        from email.utils import formataddr

        # msg = MIMEText(self.Template.format(**kwargs), 'html', self.MailConfig.value['Ecoding'])
        msg = MIMEText(self.Template, 'html', self.MailConfig.value['Ecoding'])
        msg['From'] = formataddr(pair=(self.MailConfig.value['FromName'], self.config['Email']))
        # 给多用户发送邮件
        msg['To'] = ','.join(self.ToMail)
        msg['cc'] = ','.join(self.MailConfig.value['cc'])
        msg['Subject'] = '您的评论有新的回复'
        return msg

    async def send(self, **kwargs):
        await self.init_config()
        smtp = None
        import smtplib
        try:
            smtp = smtplib.SMTP_SSL(self.config['Host'], self.config['Port'])
            smtp.login(self.config['Email'], self.config['Password'])
            smtp.sendmail(self.config['Email'], self.ToMail, self._content(**kwargs).as_string())
        except TimeoutError:
            print('连接服务器失败')
        except smtplib.SMTPAuthenticationError:
            print('用户名密码验证失败')
        except smtplib.SMTPException as e:
            print('发送失败:', e)
        finally:
            smtp.quit()

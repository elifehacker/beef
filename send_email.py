
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os,datetime
from bs4 import BeautifulSoup

def send_report(to_email):
    CRLF = "\r\n"
    login = "chatbot9900@gmail.com"
    password = "Chat#9900"
    report="dailyreport.html"
    # attendees = ["chatbot9900@gmail.com", "e.life.hacker@gmail.com"]
    organizer = "ORGANIZER;CN=organiser:mailto:chatbot9900"+CRLF+" @gmail.com"
    fro = "Chatbot9900 <chatbot9900@gmail.com>"

    eml_body = "Please find report attached"


    eml_body_bin = "This is the email body in binary - two steps"
    msg = MIMEMultipart('mixed')
    msg['Reply-To']=fro
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Daily report"
    msg['From'] = fro
    msg['To'] = to_email

    part_email = MIMEText(eml_body,"html")  

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    msgAlternative.attach(part_email)

    with open(report, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {report}",
    )
    msg.attach(part)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(login, password)
    mailServer.sendmail(fro, to_email, msg.as_string())
    mailServer.close()

if __name__ == "__main__":
    send_report('steven_wang_pei@hotmail.com')   
    
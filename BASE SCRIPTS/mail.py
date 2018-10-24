#  Created by Bogdan Trif on 21-08-2018 , 4:16 PM.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# fromaddr = "mail_address1@gmail.com"
# toaddr = "mail_address2@gmail.com"

# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "SUBJECT OF THE MAIL"
#

# try :
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(fromaddr, "password")
#     text = msg.as_string()
#     server.sendmail(fromaddr, toaddr, text)
#     server.quit()
#
# except Exception :
#     print( "Error: unable to send email")

import smtplib

def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)

    header += 'Subject: %s\n\n' % subject
    message = header + message
    try :
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login, password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
        return problems
    except Exception :
        print( "Error: unable to send email")


coin = 'XRP'
percent = -1.34
msg = coin +  """  just crashed  , percent =  """ +str(percent) +"%  "

# msg = MIMEMultipart()
# msg.attach(MIMEText(body, 'plain'))



sendemail(
         from_addr    = 'market ALERT ',
          to_addr_list = ['mail_to_Send_to@gmail.com'],

          subject      = coin + "  " + str(percent) +" %"  ,
          message      = msg ,
          login        =    'login_mail',
          password     = 'password'
)
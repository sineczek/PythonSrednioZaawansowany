import smtplib
mailFrom = 'Your automation system'
mailTo = 'mail@mail.com', 'poczta@poczta.pl'
mailSubject = 'Processing done'
body = 'treść'

message = '''From: {}
Subject: {}

{}'''.format(mailFrom,mailSubject,body)

user = 'mail1@mail.com'
password = '1234'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehio()
    server.login(user,password)
    server.sendmail(user,mailTo,message)
    server.close()
    print('mail sent')
except:
    print('error sending mail')







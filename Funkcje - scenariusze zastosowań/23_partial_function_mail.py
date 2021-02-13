import smtplib
import functools


def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = '''From: {}
Subject: {}
    
{}
'''.format(mailFrom,mailSubject,mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehio()
        server.login(user,password)
        server.sendmail(user,mailTo,message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending mail')
        return False


mailFrom = 'Your automation system'
mailTo = 'mail@mail.com', 'poczta@poczta.pl'
mailSubject = 'Processing done'
mailBody = 'treść'

user = 'mail1@mail.com'
password = '1234'

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password, mailSubject = 'Execution alert!')

SendInfoEmailFromGmail(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)



#SendInfoEmail(user,password,mailFrom,mailTo,mailSubject,mailBody)

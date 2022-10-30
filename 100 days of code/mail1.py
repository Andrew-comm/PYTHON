#trying to connect  server gives error needs ssl to work
import mailbox
import smtplib
import getpass

mail_server = smtplib.SMTP_SSL('localhost')

#inorder to see messages being sent back and forth 
mail_server.set_debuglevel(1)

#to authenticate

mail_pass = getpass.getpass('password1')
print(mail_pass)

mail_server.login(mail_pass)
(235, b'2.7.0 Accepted')
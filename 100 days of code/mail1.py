#!/usr/bin/env python3
import mimetypes
import mailbox
import smtplib
import getpass
import os.path
import email.message 

def generate(sender, recipient, subject, body, attachment_path):

    ##"""creates an email with attachment"""

    #basic email formatting
    sender = "localhost"
    recipient = "you@example.com"
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)


    #process attachment and add it to email

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _= mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/',1)


    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                        
                            maintype = mime_type,
                            subtype = mime_subtype,
                            filename = attachment_filename)

        return message

#to authenticate
mail_pass = getpass.getpass('password1')
print(mail_pass)






def send(message):
    mail_server = smtplib.SMTP_SSL('localhost')

    mail_server.login(sender, mail_pass)

#inorder to see messages being sent back and forth 
    mail_server.set_debuglevel(1)
    mail_server.send_message(message)
    mail_server.quit()
    


    










 

# mail_server.login(mail_pass)
# (235, b'2.7.0 Accepted')
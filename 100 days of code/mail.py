
from email.message import EmailMessage
message = EmailMessage

sender = "me@example.com"
recipient = "you@example.com"

message = 'Greetings from {} to {}!'.format(sender, recipient)
#message = "sender: {} \n recipient: {}".format(sender,recipient)
body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)
print(message)






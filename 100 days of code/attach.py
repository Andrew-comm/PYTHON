#!/usr/bin/env python3

import os.path
from email.message import EmailMessage
from email.message import *
message = EmailMessage
attachment_path = "/home/andrea/Pictures/Screenshots/Screenshot from 2022-09-30 01-12-21.png"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

#separate
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)

print(mime_subtype)


with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
print(message)

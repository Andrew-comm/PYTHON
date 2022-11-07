#!/usr/bin/env python3

import mail1
import os
import report
#two modules reports and mail1 to create a report1 and then send it by email.
table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48]]
report.generate("/tmp/report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

sender = "sender@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

message = mail1.generate(sender, receiver, subject, body, "/tmp/report.pdf")
mail1.send(message)

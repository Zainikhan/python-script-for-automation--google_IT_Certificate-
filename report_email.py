#!/usr/bin/env python3

import os 
import datetime
import reports
import emails


def pdf_context(path):
  '''This functions read all the files in given directory and return string only of the first 2 linesof all files with <br /> added so we can genrate good pdf'''
  fruits = ""
  for file_name in os.listdir(path):
    with open(path+"/"+file_name) as file:
       file_context = file.readlines()
       name = file_context[0].strip('\n')
       weight = file_context[1].strip('\n')
       fruits += "name: {}".format(name)+ '<br />'+ "weight: {}".format(weight)+"<br />" + "<br />"
  return fruits

if __name__ == "__main__":
  path = os.path.expanduser('~') + "/supplier-data/descriptions"
  current_date = datetime.date.today().strftime("%B %d, %Y")  # Creating data in format "July 13, 2020"
  title = "Processed Update on "+str(current_date)
  reports.generate_report('/tmp/processed.pdf', title, pdf_context(path))
  email_subject = 'Upload Completed - Online Fruit Store'  # subject line give in assignment for email
  email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # body line give in assignment for email
  msg = emails.generate_email("automation@example.com", "{}@example.com".format(os.getenv('USER')),
                         email_subject, email_body, "/tmp/processed.pdf")  # structuring email and attaching the file. Then sending the email, using the cus$
  emails.send_email(msg)

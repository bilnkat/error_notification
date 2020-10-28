#!/usr/bin/env python3

import shutil
import psutil
import email
import smtplib

disk_usage = shutil.disk_usage('/')
percent_free = disk_usage[2]/disk_usage[0] * 100
free_memory = psutil.virtual_memory()[1] / 1000000
localhost_key = list(psutil.net_if_addrs().keys())[0]
localhost = psutil.net_if_addrs()[localhost_key][0][1]

sender = 'automation@example.com'
recipient = 'user0@example.com'
body = 'Please check your system and resolve the issue as soon as possible.'


def generate_error_report(sender, recipient, subject, body):
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()

if psutil.cpu_percent(3) > 80:
    subject = 'Error - CPU usage is over 80%'
    generate_error_report(sender, recipient, subject, body)

if percent_free < 20:
    subject = 'Error - Available disk space is less than 20%'
    generate_error_report(sender, recipient, subject, body)

if free_memory < 500:
    subject = 'Error - Available memory is less than 500MB'
    generate_error_report(sender, recipient, subject, body)

if localhost != '127.0.0.1':
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    generate_error_report(sender, recipient, subject, body)


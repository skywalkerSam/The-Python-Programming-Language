"""
Developer: Sam Skywalker
Purpose: Learning
Date: 

"""

import email
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def simple_email():
    email = EmailMessage()
    email["from"] = "Sam Skywalker"
    email["to"] = "samskywalker001@gmail.com"
    email['subject'] = "First Automated Email..."

    email.set_content("This is the first automated email ever created by myself ;)")

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('samskywalker.asaiinc@gmail.com', 'passwordORkey')
        smtp.send_message(email)
        print('\n\t All Good, Email Sent :) \n')


# simple_email()


def second_email():
    email = EmailMessage()
    email['from'] = 'Sam Skywalker'
    email['to'] = 'samskywalker001@gmail.com'
    email['subject'] = 'Second Automated Email...'

    email_content = Template(Path('content.html').read_text())
    email.set_content(email_content.substitute(name='Starboy', ai_system='Cortana AI'), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('samskywalker.asaiinc@gmail.com', 'passwordORkey')
        smtp.send_message(email)
        print('\n\t Successful, Email Sent :) \n')


# second_email()


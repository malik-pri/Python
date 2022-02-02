import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'your name'
email['to'] = 'senders email'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am Python Master!! HAHAHAHA')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your email', 'your password')
    smtp.send_message(email)
    print('All good boo!')


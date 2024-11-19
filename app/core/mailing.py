from aiosmtplib import SMTP
import asyncio

from email.message import EmailMessage

import os
from dotenv import load_dotenv

load_dotenv()

async def auth_mail(user_email, secret_key):
    message = EmailMessage()
    message['From'] = os.getenv('SMTP_USER')
    message["To"] = user_email
    message["Subject"] = "[NF MISIS BOT] Ваш код подтверждения"
    message.set_content(f'Ваш код для подтверждения почты: \n\n{secret_key}')

    smtp = SMTP(hostname=os.getenv('SMTP_HOST'), port=os.getenv('SMTP_PORT'), use_tls=True)

    await smtp.connect()
    await smtp.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASSWORD'))
    await smtp.send_message(message)
    await smtp.quit()
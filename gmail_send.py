import requests
import os
from dotenv import load_dotenv

load_dotenv()

SCRIPT_URL = os.getenv('APP_SCRIPT_URL')

def send_email(to, subject, body):

    data = {
        'to':to,
        'subject':subject,
        'body':body
    }

    response = requests.post(SCRIPT_URL, json=data)

    return response.text

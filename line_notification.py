import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_line_notification(message, file=None):
    line_notify_token = os.getenv("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"

    headers = {"Authorization": f"Bearer {line_notify_token}"}
    payload = {"message": message}

    if file:
        files = {"imageFile": open(file, "rb")}
        response = requests.post(line_notify_api, headers=headers, data=payload, files=files)
    else:
        response = requests.post(line_notify_api, headers=headers, data=payload)
        
    response.raise_for_status()

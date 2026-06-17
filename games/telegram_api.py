import requests
from django.conf import settings


def send_telegram_message(message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID

    url = f"https://api.telegram.org/bot{8785011131:AAHOHYKsubUSLZp25OBfow6iCqCGF_gWWyU}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=data, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print("Telegram Error:", e)
        return False
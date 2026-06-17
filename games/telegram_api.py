from django.conf import settings
import requests

def send_telegram_message(message):

    print("TOKEN =", settings.TELEGRAM_BOT_TOKEN)
    print("CHAT_ID =", settings.TELEGRAM_CHAT_ID)

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

    print("URL =", url)

    response = requests.post(
        url,
        data={
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": message,
        }
    )

    print("STATUS =", response.status_code)
    print("BODY =", response.text)

    return response.status_code == 200
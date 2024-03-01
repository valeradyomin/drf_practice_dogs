import requests

from config import settings


class MyTelegramBot:
    URL = "https://api.telegram.org/bot"
    TOKEN = settings.TELEGRAM_BOT_TOKEN

    def send_message(self, text):
        requests.post(
            url=f"{self.URL}{self.TOKEN}/sendMessage",
            data={
                "chat_id": '102353389',
                "text": text,
            },
        )
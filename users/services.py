import requests

from config import settings


class MyTelegramBot:
    URL = 'https://api.telegram.org/bot'
    # TOKEN = settings.TELEGRAM_BOT_TOKEN
    # CHAT_ID = settings.TELEGRAM_BOT_CHAT_ID
    TOKEN = ''
    CHAT_ID = ''

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.CHAT_ID,
                'text': text
            },
        )


bot = MyTelegramBot()
cht_id = bot.CHAT_ID
token = bot.TOKEN

print(token)
print(cht_id)

bot.send_message(text='Hi, Sky!')

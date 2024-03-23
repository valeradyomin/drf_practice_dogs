import requests

from config import settings


class MyTelegramBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_BOT_TOKEN
    CHAT_ID = settings.TELEGRAM_BOT_CHAT_ID

    def send_message(self, text):
        # proxies = {
        #     'http': 'socks5://43.155.170.35:15673',
        #     'https': 'socks5://43.155.170.35:15673'
        # }
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.CHAT_ID,
                'text': text
            },
            verify=False, proxies=None)


bot = MyTelegramBot()
cht_id = bot.CHAT_ID
token = bot.TOKEN

print(token)
print(cht_id)

bot.send_message(text='Hi, Sky!')

from django.core.management.base import BaseCommand

from users.services import MyTelegramBot


class Command(BaseCommand):
    def handle(self, *args, **options):
        my_bot = MyTelegramBot()
        my_bot.send_message('Hi, Sky!')

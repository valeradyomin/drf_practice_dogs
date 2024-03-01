import datetime

from celery import shared_task

from app_dogs.models import Dog


@shared_task
def send_message_about_like(chat_id):
    print(f'сообщение о лайке отправлено в чат {chat_id}')


def send_mail_about_birthday():
    dog_list = Dog.objects.filter(birthday=datetime.date.today())
    for dog in dog_list:
        print(f'Send mail about {dog} birthday to {dog.owner.username}')
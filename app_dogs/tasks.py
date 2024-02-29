from celery import shared_task


@shared_task
def send_message_about_like(chat_id):
    print(f'сообщение о лайке отправлено в чат {chat_id}')

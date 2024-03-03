import telebot

from config import settings

# Получаем токен бота из переменной окружения
bot_token = settings.TELEGRAM_BOT_TOKEN

# Создаем экземпляр бота
bot = telebot.TeleBot(bot_token)

# Отправляем сообщение
chat_id = settings.TELEGRAM_BOT_CHAT_ID  # Замените на ваш chat_id
text = 'Привет, мир!'
bot.send_message(chat_id, text, timeout=30)  # Устанавливаем таймаут в 10 секунд

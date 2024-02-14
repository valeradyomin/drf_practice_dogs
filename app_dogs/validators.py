from rest_framework.serializers import ValidationError

SCAM_WORDS = ['крипта', 'биржа', 'продам', 'валюта']


def validator_scam_words(value):
    """
    Функция, которая проверяет содержит ли входное значение какие-либо запрещенные слова и вызывает исключение
    ValidationError, если содержит. Параметры: value: str - входная строка, которую нужно проверить на наличие
    запрещенных слов
    """
    if set(value.lower().split()) & set(SCAM_WORDS):
        raise ValidationError('Текст содержит запрещенные слова')

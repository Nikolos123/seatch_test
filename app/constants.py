"""Модуль для описания констант приложения."""
from typing import Final

#: Путь для API
API_V1_PATH: Final[str] = '/api/v1'
#: Наименование API ключа по дефолту
API_KEY_NAME: Final[str] = 'X-Auth-Key'
#: Наименьшее значение длины наименования провайдера
MIN_LENGTH_OF_PROVIDER_NAME: Final[int] = 2
#: Наибольшее значение длины наименования провайдера
MAX_LENGTH_OF_PROVIDER_NAME: Final[int] = 50
#: Наименьшее значение длины API ключа для провайдера
MIN_LENGTH_OF_PROVIDER_API_KEY: Final[int] = 12
#: Наибольшее значение длины API ключа для провайдера
MAX_LENGTH_OF_PROVIDER_API_KEY: Final[int] = 50
#: Наименьшее значение длины наименования API ключа
MIN_LENGTH_OF_API_KEY_NAME: Final[int] = 5
#: Наибольшее значение длины наименования API ключа
MAX_LENGTH_OF_API_KEY_NAME: Final[int] = 20

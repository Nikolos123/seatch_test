"""Модуль для описания конфига приложения.

DSN - Data Source Name.
"""
from functools import lru_cache
from dotenv import find_dotenv

from pydantic import BaseSettings, Field, PostgresDsn


class Settings(BaseSettings):
    """Конфиг приложения."""

    PERSISTENCE_DSN: PostgresDsn = Field(title='DSN для доступа к базе данных')
    # AMQP_DSN: AmqpDsn = Field(title='DSN для доступа к очереди сообщений')
    # PROVIDER_API_KEYS: ProviderApiKeys = Field(title='API ключи для провайдеров')
    # API_KEY_NAME: ApiKeyName = Field(default=KEY_NAME, title='Наименование API ключа')
    # HTTP_BASIC_USERNAME: StrictStandardString = Field(title='Имя для Http Basic Auth')
    # HTTP_BASIC_PASSWORD: StrictStandardString = Field(title='Пароль для Http Basic Auth')


class SettingsFromFile(Settings):
    """Конфиг приложения, получаемый из файла."""

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    """Возвращает объект конфига приложения.

    Детектирование среды разработки.

    Если в корневой директории есть dotenv файл (.env), то это трактуется как вариант для локальной разработки. Все
    переменные окружения будут браться из этого файла.

    В остальных случаях считается, что разработка ведется в контейнере и все переменные окружения будут браться из
    системы контейнера.

    Результат работы функции будет закеширован при первом вызове.
    """
    try:
        find_dotenv(filename='.env', raise_error_if_not_found=True)
    except Exception as f:
        return Settings()
    return SettingsFromFile()

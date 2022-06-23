"""Модуль для описания конфига схем валидации данных договоров страхования."""


def snake_case_to_camel_case(snake_case: str) -> str:
    """Конвертация snake_case в camelСase."""
    first, *others = snake_case.split('_')
    return ''.join(
        [first.lower(), *(word.capitalize() for word in others)],
    )


class BaseConfig(object):
    """Базовый мета конфиг для Schemas классов."""

    # разрешает полю с алиасом быть заполненным как значением по алиасу, так и
    # по его наименованию
    allow_population_by_field_name = True
    # генерация алиасов для отображения на фронтенде
    alias_generator = snake_case_to_camel_case

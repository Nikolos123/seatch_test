from typing import TypedDict


class InsurantDto(TypedDict):
    """Данные клиента (страхователя) в основном сервисе."""

    pk: int
    first_name: str
    second_name: str
    last_name: str
    birthday: str
    inn: str

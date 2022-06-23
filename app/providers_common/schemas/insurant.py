"""Модуль для описания схем валидации данных договоров страхования жизни."""

from app.providers_common.aliases import OptionalStrictStandardString, StrictStandardString
from pydantic import BaseModel, Field


class IsurantSchema(BaseModel):
    """Базовая схема валидации для договора страхования жизни."""

    insurant_inn: OptionalStrictStandardString = Field(
        title='Идентификационный номер налогоплательщика (страхователя)', default='',
    )
    first_name: StrictStandardString = Field(title='Имя')
    second_name: OptionalStrictStandardString = Field(
        title='Отчество', default='',
    )
    last_name: StrictStandardString = Field(title='Фамилия')
    birthday: StrictStandardString = Field(
        title='День рождения', default='',
    )

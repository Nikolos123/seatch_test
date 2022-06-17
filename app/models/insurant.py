from sqlalchemy import Column, Integer, String

from seatch_test.app.models.base import BaseModel


class Insurant(BaseModel):
    """Модель данных клиента (страхователя) в основном сервисе."""

    __tablename__ = 'clientprofile'

    id = Column(Integer, primary_key=True)
    inn = Column(String)

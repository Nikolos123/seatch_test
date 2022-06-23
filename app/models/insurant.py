from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String


class Insurant(BaseModel):
    """Модель данных клиента (страхователя) в основном сервисе."""

    __tablename__ = 'clientprofile'

    id = Column(Integer, primary_key=True)
    inn = Column(String)
    fst_name = Column(String)
    lst_name = Column(String)
    mid_name = Column(String)
    birth_date = Column(String)

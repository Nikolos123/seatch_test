from app.providers_common.schemas.config import BaseConfig
from app.providers_common.schemas.insurant import IsurantSchema


class InvestmentUseCaseRequest(IsurantSchema):
    """Запрос с валидацией данных по договору ИСЖ."""

    class Config(BaseConfig):
        """Мета конфиг схемы валидации для договора ИСЖ."""

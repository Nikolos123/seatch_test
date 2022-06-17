from pydantic import BaseModel


class FindInsurantByInnGatewayQueryRequest(BaseModel):
    """Запроса на поиск клиента (страхователя) по его ИНН."""

    inn: str

from pydantic import BaseModel


class FindInsurantByDataGatewayQueryRequest(BaseModel):
    """Запроса на поиск клиента (страхователя) по его ФИ,ДР"""

    inn: str
    first_name:str
    second_name:str
    last_name:str
    birthday:str

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from seatch_test.app.gateways.dtos.insurant import InsurantDto
from seatch_test.app.gateways.queries.requests.insurant import FindInsurantByInnGatewayQueryRequest
from seatch_test.app.models.insurant import Insurant


class FindInsurantByInnGatewayQueryHandler:
    """Обработчик запроса на поиск клиента (страхователя) по его ИНН."""

    __slots__ = ('_session',)

    def __init__(self, session: Session) -> None:
        self._session = session

    def handle(self, request: FindInsurantByInnGatewayQueryRequest) -> InsurantDto:
        """Запуск поиска клиента (страхователя).

        :param request: Запроса на поиск клиента (страхователя) по его ИНН.
        :return: Данные клиента (страхователя).
        """
        insurant = self._session.query(Insurant.id).filter(
            Insurant.inn == request.inn,
        ).first()
        if not insurant:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Insurant not found.')
        return InsurantDto(pk=insurant.id)

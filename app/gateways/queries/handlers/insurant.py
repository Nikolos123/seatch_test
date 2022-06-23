from fastapi import HTTPException
from app.gateways.dtos.insurant import InsurantDto
from app.gateways.queries.requests.insurant import FindInsurantByDataGatewayQueryRequest
from app.models.insurant import Insurant
from sqlalchemy.orm import Session
from starlette import status


class FindInsurantByDataGatewayQueryHandler:
    """Обработчик запроса на поиск клиента (страхователя) по его ФИ,ДР."""

    __slots__ = ('_session',)

    def __init__(self, session: Session) -> None:
        self._session = session

    def handle(self, request: FindInsurantByDataGatewayQueryRequest) -> list:
        """Запуск поиска клиента (страхователя).

        :param request: Запроса на поиск клиента (страхователя) по его ИНН.
        :return: Данные клиента (страхователя).
        """
        insurant = self._session.query(
            Insurant.id, Insurant.inn,
            Insurant.mid_name, Insurant.fst_name,
            Insurant.lst_name,
            Insurant.birth_date,
        ).filter(
            Insurant.birth_date == request.birthday,
            Insurant.lst_name == request.last_name,
            Insurant.fst_name == request.first_name,
        )
        if not insurant.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Insurant not found.')
        if insurant.count() > 1:
            for profile_ in insurant:
                if request.inn == profile_.inn:
                    return InsurantDto(
                        pk=profile_.id,
                        first_name=profile_.fst_name,
                        second_name=profile_.mid_name,
                        last_name=profile_.lst_name,
                        birthday=profile_.birth_date,
                        inn=profile_.inn,
                    )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Insurant not found.',
            )
        else:
            profile = insurant.first()
        return InsurantDto(
            pk=profile.id,
            first_name=profile.fst_name,
            second_name=profile.mid_name,
            last_name=profile.lst_name,
            birthday=profile.birth_date,
            inn=profile.inn,

        )

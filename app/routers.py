"""Модуль для описания роутов приложения."""
from typing import Dict

from app.constants import API_V1_PATH
from app.db import get_db_session
from fastapi import APIRouter, Depends, status
from app.gateways.queries.handlers.insurant import FindInsurantByDataGatewayQueryHandler
from sqlalchemy.orm import Session
from app.usecases.handlers.get_user import ProcessGetUser
from app.usecases.requests.get_user import InvestmentUseCaseRequest

responses: Dict = {
    status.HTTP_403_FORBIDDEN: {'description': 'Not authenticated'},
    status.HTTP_404_NOT_FOUND: {'description': 'Entity no found.'},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {'description': 'Internal Server Error.'},
}
router = APIRouter()


@router.post(
    f'{API_V1_PATH}/user/',
    status_code=status.HTTP_200_OK,
    responses=responses,
    response_model=InvestmentUseCaseRequest,
)
def user(
    contract: InvestmentUseCaseRequest,
    session: Session = Depends(get_db_session),
):
    """Проверка юзера в основной базе."""
    ProcessGetUser(
        client_finding_by_inn=FindInsurantByDataGatewayQueryHandler(session),
    ).handle(contract)
    return contract

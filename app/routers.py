"""Модуль для описания роутов приложения."""
from typing import Dict

from fastapi import APIRouter, Depends, status
from pika import BlockingConnection
from sqlalchemy.orm import Session

from app.amqp import get_amqp_connection
from seatch_test.app.constants import API_KEY_NAME, API_V1_PATH
from app.db import get_db_session
from app.gateways.commands.handlers.contract import SendContractToAmqpGatewayCommandHandler
from seatch_test.app.gateways.queries.handlers.insurant import FindInsurantByInnGatewayQueryHandler
from seatch_test.app.security import APIKeyCredentials, APIKeyHeader
from app.usecases.handlers.investment_contract import ProcessInvestmentContractUseCaseHandler
from app.usecases.requests.investment_contract import InvestmentContractUseCaseRequest

responses: Dict = {
    status.HTTP_403_FORBIDDEN: {'description': 'Not authenticated'},
    status.HTTP_404_NOT_FOUND: {'description': 'Entity no found.'},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {'description': 'Internal Server Error.'},
}
router = APIRouter()
security = APIKeyHeader(name=API_KEY_NAME, description='Ключ для доступа к API')


@router.get(
    f'{API_V1_PATH}/contracts/investment/',
    status_code=status.HTTP_200_OK,
    responses=responses,
    response_model=InvestmentContractUseCaseRequest,
)
def investment_contract(
    contract: InvestmentContractUseCaseRequest,
    credentials: APIKeyCredentials = Depends(security),
    session: Session = Depends(get_db_session),
    amqp_connection: BlockingConnection = Depends(get_amqp_connection),
):
    """Создание (обновление) договора страхования ИСЖ."""
    contract._credentials = credentials
    ProcessInvestmentContractUseCaseHandler(
        client_finding_by_inn=FindInsurantByInnGatewayQueryHandler(session),
        appending_to_queue=SendContractToAmqpGatewayCommandHandler(amqp_connection),
    ).handle(contract)
    return contract


# @router.post(
#     '{api_path}/contracts/universal/'.format(api_path=API_V1_PATH),
#     status_code=status.HTTP_201_CREATED,
#     responses=responses,
#     response_model=UniversalContractUseCaseRequest,
# )
# def universal_contract(
#     contract: UniversalContractUseCaseRequest,
#     credentials: APIKeyCredentials = Depends(security),
#     session: Session = Depends(get_db_session),
#     amqp_connection: BlockingConnection = Depends(get_amqp_connection),
# ):
#     """Создание (обновление) договора страхования НСЖ."""
#     contract._credentials = credentials
#     ProcessUniversalContractUseCaseHandler(
#         client_finding_by_inn=FindInsurantByInnGatewayQueryHandler(session),
#         appending_to_queue=SendContractToAmqpGatewayCommandHandler(amqp_connection),
#     ).handle(contract)
#     return contract
#
#
# @router.post(
#     path='{api_path}/payments/actual/'.format(api_path=API_V1_PATH),
#     status_code=status.HTTP_201_CREATED,
#     responses=responses,
#     response_model=ActualPaymentsRequest,
# )
# def actual_payments(
#     payments: ActualPaymentsRequest,
#     credentials: APIKeyCredentials = Depends(security),
#     amqp_connection: BlockingConnection = Depends(get_amqp_connection),
# ):
#     """Создание (обновление) фактических платежей по договору НСЖ."""
#     payments._credentials = credentials
#     ProcessActualPaymentsUseCaseCommandHandler(
#         appending_to_amqp=SendPaymentsToAmqpGatewayCommandHandler(amqp_connection),
#     ).handle(request=payments)
#     return payments
#
#
# @router.post(
#     path='{api_path}/payments/scheduled/'.format(api_path=API_V1_PATH),
#     status_code=status.HTTP_201_CREATED,
#     responses=responses,
#     response_model=ScheduledPaymentsRequest,
# )
# def scheduled_payments(
#     payments: ScheduledPaymentsRequest,
#     credentials: APIKeyCredentials = Depends(security),
#     amqp_connection: BlockingConnection = Depends(get_amqp_connection),
# ):
#     """Создание (обновление) платежей по календарю договора НСЖ."""
#     payments._credentials = credentials
#     ProcessScheduledPaymentsUseCaseCommandHandler(
#         appending_to_amqp=SendPaymentsToAmqpGatewayCommandHandler(amqp_connection),
#     ).handle(request=payments)
#     return payments

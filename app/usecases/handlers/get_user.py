from app.gateways.dtos.insurant import InsurantDto
from app.gateways.interfaces import IGatewayHandleable
from app.gateways.queries.requests.insurant import FindInsurantByDataGatewayQueryRequest
from app.usecases.requests.get_user import InvestmentUseCaseRequest


class ProcessGetUser:
    """Сценарий получения юзера из бд."""

    def __init__(
        self,
        client_finding_by_inn: IGatewayHandleable[FindInsurantByDataGatewayQueryRequest, InsurantDto],

    ):
        self._client_finding_by_inn = client_finding_by_inn

    def handle(self, request: InvestmentUseCaseRequest) -> None:
        insurant = self._client_finding_by_inn.handle(
            FindInsurantByDataGatewayQueryRequest(
                inn=request.insurant_inn,
                first_name=request.first_name,
                second_name=request.second_name,
                birthday=request.birthday,
                last_name=request.last_name,
            ),
        )
        return insurant

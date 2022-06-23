"""Модуль для описания общих интерфейсов данных для Gateways."""
from typing import Protocol, runtime_checkable

from app.gateways.types import GatewayRequest, GatewayResponse


@runtime_checkable
class IGatewayHandleable(Protocol[GatewayRequest, GatewayResponse]):
    """Общий интерфейс обработчика запросов к источникам данных."""

    __slots__ = ()

    def handle(self, request: GatewayRequest) -> GatewayResponse:
        """Запуск обработки внешнего запроса к источникам данных.

        :param request: Данные внешнего запроса.
        :return: Результат обработки внешнего запроса
        """

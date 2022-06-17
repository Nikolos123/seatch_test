"""Модуль для описания безопасности и доступа к приложению."""
from typing import Optional

from fastapi.openapi.models import APIKey, APIKeyIn
from fastapi.security.api_key import APIKeyBase
from pydantic import BaseModel
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from seatch_test.app.config import Settings, get_settings


class APIKeyCredentials(BaseModel):
    """Верительные данные при авторизации по ключу API."""

    provider: str
    api_key: str


class APIKeyHeader(APIKeyBase):
    """Проверка наличия в заголовках ключа API."""

    __slots__ = ('auto_error', 'settings')

    def __init__(
        self,
        *,
        name: str,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
        settings: Settings = get_settings(),
    ):
        self.model: APIKey = APIKey(**{'in': APIKeyIn.header}, name=name, description=description)
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error
        self.settings = settings

    async def __call__(self, request: Request) -> Optional[APIKeyCredentials]:
        api_key: str = request.headers.get(self.model.name)
        if api_key:
            for provider, key in self.settings.PROVIDER_API_KEYS.items():
                if key == api_key:
                    return APIKeyCredentials(provider=provider, api_key=key)
        if self.auto_error:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Not authenticated')
        return None

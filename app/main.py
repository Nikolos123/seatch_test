"""Модуль для описания запуска приложения."""
import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse

from seatch_test.app.config import Settings, get_settings
from seatch_test.app.constants import API_V1_PATH
from seatch_test.app.routers import router

OPEN_API_JSON_PATH: str = '{path}/openapi.json'.format(path=API_V1_PATH)
__version__ = '0.5.0'
__title__ = 'Providers API'

application = FastAPI(
    title=__title__,
    version=__version__,
    openapi_url=None,
    docs_url=None,
    redoc_url=None,
)
application.include_router(router)


def check_credentials(
    credentials: HTTPBasicCredentials = Depends(HTTPBasic()),
    settings: Settings = Depends(get_settings),
) -> HTTPBasicCredentials:
    """Проверяет доступ по Http Basic Auth.

    Используется только для доступа к документации.
    """
    is_correct_username = secrets.compare_digest(credentials.username, settings.HTTP_BASIC_USERNAME)
    is_correct_password = secrets.compare_digest(credentials.password, settings.HTTP_BASIC_PASSWORD)
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Basic'},
        )
    return credentials


@application.get(OPEN_API_JSON_PATH, include_in_schema=False)
def open_api(credentials: HTTPBasicCredentials = Depends(check_credentials)):
    """Схема OpenAPI."""
    return JSONResponse(get_openapi(title=__title__, version=__version__, routes=application.routes))


@application.get('{path}/docs'.format(path=API_V1_PATH), include_in_schema=False)
def swagger(credentials: HTTPBasicCredentials = Depends(check_credentials)):
    """Документация в стиле Swagger."""
    return get_swagger_ui_html(openapi_url=OPEN_API_JSON_PATH, title=__title__)


@application.get('{path}/redoc'.format(path=API_V1_PATH), include_in_schema=False)
def redoc(credentials: HTTPBasicCredentials = Depends(check_credentials)):
    """Документация в стиле ReDoc."""
    return get_redoc_html(openapi_url=OPEN_API_JSON_PATH, title=__title__)

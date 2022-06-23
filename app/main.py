"""Модуль для описания запуска приложения."""
import uvicorn

from app.constants import API_V1_PATH
from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from app.routers import router
from starlette.responses import JSONResponse

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


@application.get(OPEN_API_JSON_PATH, include_in_schema=False)
def open_api():
    """Схема OpenAPI."""
    return JSONResponse(get_openapi(title=__title__, version=__version__, routes=application.routes))


@application.get('{path}/docs'.format(path=API_V1_PATH), include_in_schema=False)
def swagger():
    """Документация в стиле Swagger."""
    return get_swagger_ui_html(openapi_url=OPEN_API_JSON_PATH, title=__title__)


@application.get('{path}/redoc'.format(path=API_V1_PATH), include_in_schema=False)
def redoc():
    """Документация в стиле ReDoc."""
    return get_redoc_html(openapi_url=OPEN_API_JSON_PATH, title=__title__)

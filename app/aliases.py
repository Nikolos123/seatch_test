"""Модуль для описания алиасов типов приложения."""
from typing import Dict

from pydantic import constr

from seatch_test.app.constants import (
    MAX_LENGTH_OF_API_KEY_NAME,
    MAX_LENGTH_OF_PROVIDER_API_KEY,
    MAX_LENGTH_OF_PROVIDER_NAME,
    MIN_LENGTH_OF_API_KEY_NAME,
    MIN_LENGTH_OF_PROVIDER_API_KEY,
    MIN_LENGTH_OF_PROVIDER_NAME,
)

ProviderName = constr(strict=True, min_length=MIN_LENGTH_OF_PROVIDER_NAME, max_length=MAX_LENGTH_OF_PROVIDER_NAME)
ProviderApiKey = constr(
    strict=True,
    min_length=MIN_LENGTH_OF_PROVIDER_API_KEY,
    max_length=MAX_LENGTH_OF_PROVIDER_API_KEY,
)
ProviderApiKeys = Dict[ProviderName, ProviderApiKey]
ApiKeyName = constr(strict=True, min_length=MIN_LENGTH_OF_API_KEY_NAME, max_length=MAX_LENGTH_OF_API_KEY_NAME)

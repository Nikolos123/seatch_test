"""Модуль, содержащий алиасы типов для pydantic моделей."""
from app.providers_common.constants import STANDARD_MAX_LENGTH_OF_STRING, STANDARD_MIN_LENGTH_OF_STRING
from pydantic import constr

# Строгая стандартная строка размером 1 < x < 255 символов, очисткой от
# пробелов
StrictStandardString = constr(
    strict=True,
    min_length=STANDARD_MIN_LENGTH_OF_STRING,
    max_length=STANDARD_MAX_LENGTH_OF_STRING,
    strip_whitespace=True,
)

# Строгая стандартная строка размером 0 < x < 255 символов, очисткой от
# пробелов
OptionalStrictStandardString = constr(
    strict=True,
    max_length=STANDARD_MAX_LENGTH_OF_STRING,
    strip_whitespace=True,
)

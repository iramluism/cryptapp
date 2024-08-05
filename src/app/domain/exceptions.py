from dataclasses import dataclass
from enum import Enum


class ErrorCode(Enum):
    CRYPTO_NOT_FOUND = 404001


@dataclass
class DomainException(Exception):
    error_code: ErrorCode

    @property
    def message(self):
        return self.error_code.name

    @property
    def code(self):
        return self.error_code.value


@dataclass
class CryptoNotFoundException(DomainException):
    error_code: ErrorCode = ErrorCode.CRYPTO_NOT_FOUND

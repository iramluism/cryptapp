from fastapi import status

from app.domain.exceptions import ErrorCode

ErrorCodeMap = {
    ErrorCode.CRYPTO_NOT_FOUND: status.HTTP_404_NOT_FOUND,
}


def get_status_code(error_code: ErrorCode):
    return ErrorCodeMap.get(error_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

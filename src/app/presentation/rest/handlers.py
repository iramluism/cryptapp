from fastapi.responses import JSONResponse

from app.domain.exceptions import DomainException
from app.presentation.rest.errors import get_status_code


async def handle_domain_exception(request, exc: DomainException):
    status_code = get_status_code(exc.error_code)
    message = exc.message
    status = exc.code

    details = {
        "status": status,
        "message": message,
    }

    return JSONResponse(
        content=details,
        status_code=status_code,
    )

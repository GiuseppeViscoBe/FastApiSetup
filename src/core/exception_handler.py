import logging
from fastapi import Request
from fastapi.responses import JSONResponse

from src.core.exceptions import BaseAppException

logger = logging.getLogger(__name__)


async def base_app_exception_handler(request: Request, exc: BaseAppException):
    logger.warning(
        "Application error | path=%s | method=%s | status=%s | message=%s",
        request.url.path,
        request.method,
        exc.status_code,
        exc.message
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def integrity_error_handler(request, exc: IntegrityError):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc.orig))

from fastapi import (
    HTTPException,
    status,
)


exception_403 = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail='No access to requested operations',
    headers={
        'WWW-Authenticate': 'bearer'
    },
)

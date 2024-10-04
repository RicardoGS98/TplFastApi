import os

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

# Token secreto (este debería estar almacenado de forma segura en un entorno real)
API_TOKEN = os.environ.get('API_TOKEN')

# Se define el esquema de autenticación basado en el encabezado de la petición
api_key_header = APIKeyHeader(name="Authorization")


# Función para verificar la API Token
def verify_api_token(api_key: str = Depends(api_key_header)):
    """
    Verifica la validez del token API proporcionado en el encabezado de la solicitud.\n
    @app.get("/protected-route")\n
    def protected_route(api_key: str = Depends(verify_api_token)):
        pass

    :param api_key: Str - Token API proporcionado en el encabezado de la solicitud
    :return: Str - Token API si es válido
    """
    if api_key != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Token",
        )
    return api_key

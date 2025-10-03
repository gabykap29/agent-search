from services.agent_sql_services import agent_sql
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Dict
from fastapi import status
from fastapi import Query

class Body(BaseModel):
    query: str

    class Config:
        schema_extra = {
            "example": {
                "query": "SELECT * FROM users WHERE id = 1"
            }
        }

router = APIRouter()

@router.post(
    "/agentsql",
    summary="Ejecutar consulta con el agente SQL",
    description="Este endpoint permite enviar una consulta SQL al agente y obtener una respuesta procesada.",
    response_description="Respuesta generada por el agente en base al query.",
    responses={
        200: {
            "description": "Consulta ejecutada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "response": "Resultado generado por el agente SQL"
                    }
                }
            },
        },
        400: {"description": "Falta el parámetro query"},
        500: {"description": "Error interno al procesar la consulta"},
    },
)
def agent_sql_controller(body: Body):
    query = body.query
    if not query:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query is required")
    try:
        response = agent_sql(query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return JSONResponse(content={"response": response})

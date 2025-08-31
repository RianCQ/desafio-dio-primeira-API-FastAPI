from workout_api.contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples=['Fit Tech'], max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', examples=['Rua A, numero 307'], max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', examples=['Jonata'], max_length=30)]
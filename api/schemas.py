from pydantic import BaseModel

class Cliente(BaseModel):
    idade: int
    saldo_conta: float
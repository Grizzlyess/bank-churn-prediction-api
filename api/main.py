from fastapi import FastAPI
from api.schemas import Cliente 
import pickle
import pandas as pd

app = FastAPI()

with open('modelos/modelo.pkl', 'rb') as arquivo:
    modelo = pickle.load(arquivo)

@app.post("/predict")
def prever_churn(cliente: Cliente):
    dados = pd.DataFrame([cliente.model_dump()])
    previsao = modelo.predict(dados)[0]
    status = "Vai cancelar" if previsao == 1 else "Conta ativa"
    
    return {"previsao_churn": int(previsao), "status": status}

@app.get("/")
def pagina_inicial():
    return {"mensagem": "A API de Previsão de Churn está a funcionar corretamente!"}
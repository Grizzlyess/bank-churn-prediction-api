import pandas as pd
import pickle
from fastapi import FastAPI
from api.schemas import Cliente

app = FastAPI(title="Bank Churn API - Dados Reais")

with open('modelos/modelo.pkl', 'rb') as arquivo:
    modelo = pickle.load(arquivo)

@app.get("/")
def pagina_inicial():
    return {"mensagem": "API de Churn com modelo real ativa!"}

@app.post("/predict")
def prever_churn(cliente: Cliente):
    # O modelo espera as variáveis de texto convertidas em 0 ou 1
    dados = {
        'CreditScore': [cliente.CreditScore],
        'Age': [cliente.Age],
        'Tenure': [cliente.Tenure],
        'Balance': [cliente.Balance],
        'NumOfProducts': [cliente.NumOfProducts],
        'HasCrCard': [cliente.HasCrCard],
        'IsActiveMember': [cliente.IsActiveMember],
        'EstimatedSalary': [cliente.EstimatedSalary],
        'Geography_Germany': [1 if cliente.Geography == 'Germany' else 0],
        'Geography_Spain': [1 if cliente.Geography == 'Spain' else 0],
        'Gender_Male': [1 if cliente.Gender == 'Male' else 0]
    }
    
    df = pd.DataFrame(dados)
    previsao = modelo.predict(df)[0]
    
    status = "Vai cancelar (Alto Risco)" if previsao == 1 else "Conta ativa (Baixo Risco)"
    
    return {"previsao_churn": int(previsao), "status": status}
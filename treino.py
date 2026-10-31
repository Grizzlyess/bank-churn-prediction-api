import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

dados = {
    'idade': [25, 45, 35, 50, 23],
    'saldo_conta': [1000, 0, 5000, 0, 1200],
    'churn': [0, 1, 0, 1, 0] 
}

df = pd.DataFrame(dados)


X = df[['idade', 'saldo_conta']]
y = df['churn']


print("Treinando a Inteligência Artificial...")
modelo = RandomForestClassifier()
modelo.fit(X, y) 


with open('modelo.pkl', 'wb') as arquivo:
    pickle.dump(modelo, arquivo)

print("Sucesso!!!'")
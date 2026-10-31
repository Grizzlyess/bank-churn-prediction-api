# Bank Customer Churn Prediction API

Este projeto é uma API RESTful desenvolvida para servir um modelo de Machine Learning que prevê a probabilidade de *churn* (cancelamento de conta) de clientes bancários. Sua criação está dentro do onboarding Estágio Pagbank.

O foco deste repositório é demonstrar o ciclo completo de **MLOps e Engenharia de Software para IA**, desde o treino do modelo preditivo até ao seu empacotamento e disponibilização em produção através de contentores Docker.

## 🛠️ Tecnologias Utilizadas

*   **Machine Learning:** Python, Pandas, Scikit-Learn (Random Forest)
*   **API & Backend:** FastAPI, Uvicorn, Pydantic
*   **Infraestrutura & MLOps:** Docker, Ambientes Virtuais (venv)

## ⚙️ Arquitetura do Projeto

O projeto está dividido em duas fases principais:
1.  **Treino do Modelo (`treino.py`):** Processa os dados tabulares (idade, saldo) e treina um classificador Random Forest, exportando o modelo finalizado (ficheiro `.pkl`) utilizando a biblioteca `pickle`.
2.  **API de Inferência (`api/main.py`):** Um microsserviço construído com FastAPI que carrega o modelo pré-treinado para a memória. O endpoint recebe os dados de novos clientes via JSON, converte-os utilizando o Pandas e devolve a predição em tempo real.

## 🚀 Como Executar o Projeto

A forma recomendada de correr a aplicação é através do **Docker**, garantindo que o ambiente está totalmente isolado e reproduzível.

### Opção 1: Usando Docker (Recomendado)

1. Certifique-se de que o Docker está instalado e a correr na sua máquina.
2. Construa a imagem do contentor:
   ```bash
   sudo docker build -t churn-api .
   ```
3. Inicie o contentor mapeando a porta 8000:
   ```bash
   sudo docker run -d -p 8000:8000 churn-api
   ```
4. Aceda à documentação interativa (Swagger UI) no navegador: 
   👉 **http://localhost:8000/docs**

### Opção 2: Execução Local (Ambiente Virtual)

1. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. (Opcional) Retreine o modelo:
   ```bash
   python treino.py
   ```
4. Inicie o servidor FastAPI:
   ```bash
   uvicorn api.main:app --reload
   ```

## 📡 Utilização da API (Endpoint)

**`POST /predict`**

Recebe os dados do cliente e devolve a predição de churn.

**Corpo do Pedido (JSON):**
```json
{
  "idade": 45,
  "saldo_conta": 0.0
}
```

**Resposta de Sucesso (200 OK):**
```json
{
  "previsao_churn": 1,
  "status": "Vai cancelar"
}
```

## 🔭 Próximos Passos (Roadmap)
*   [ ] Integrar o dataset completo do Kaggle (Bank Customer Churn) com milhares de registos reais.
*   [ ] Criar um Jupyter Notebook (`.ipynb`) detalhando a Análise Exploratória de Dados (EDA).
*   [ ] Implementar métricas de avaliação do modelo (F1-Score, Matriz de Confusão).

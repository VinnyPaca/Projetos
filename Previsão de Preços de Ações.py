import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def obter_dados_acao(ticker):
    dados = yf.download(ticker, start="2015-01-01", end="2025-01-01")
    return dados

def previsao_precos(dados):
    dados['Fecha'] = dados['Close']

    dados['Dia'] = np.arange(len(dados))

    X = dados[['Dia']]  # Variável independente
    y = dados['Fecha']  # Variável dependente

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    modelo = LinearRegression()

    modelo.fit(X_train, y_train)

    previsoes = modelo.predict(X_test)

    mse = mean_squared_error(y_test, previsoes)
    print(f'Erro médio quadrático (MSE): {mse}')

    plt.figure(figsize=(10,6))
    plt.plot(dados.index, y, label="Preço Real")
    plt.plot(dados.index[-len(previsoes):], previsoes, label="Previsão", linestyle='--')
    plt.legend()
    plt.title(f'Previsão de Preços de Ações - {ticker}')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    plt.show()

ticker = 'AAPL'  # Exemplo com a ação da Apple (AAPL)
dados = obter_dados_acao(ticker)
previsao_precos(dados)

import numpy as np
import matplotlib.pyplot as plt
import requests
import yfinance as yf
import datetime

ticker = 'USDBRL=X'

hoje = datetime.datetime.now()
tres_meses_atras = hoje - datetime.timedelta(days=365)

dados = yf.download(ticker, start=tres_meses_atras.strftime('%Y-%m-%d'), end=hoje.strftime('%Y-%m-%d'))

valores = dados['Close'].values

print(valores)
proximos_valores = []

for valor in range(5):
    proximos_valores.append(valores[-1] + (valores[-1] - valores[-2]))
    
proximos_valores = np.array(proximos_valores)
valores_completos = np.append(valores, proximos_valores)

plt.plot(valores)
plt.xlabel("Dias")
plt.ylabel("Valor")
plt.title("Variação do Valor do Dólar")
plt.grid(True)
plt.show()


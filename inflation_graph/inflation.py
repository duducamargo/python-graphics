import requests
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

load_dotenv()

api_key = os.getenv('API_KEY')

url = 'https://api.stlouisfed.org/fred/series/observations'

params = {
    'series_id': 'FPCPITOTLZGBRA', 
    'api_key': api_key,  
    'file_type': 'json',
    'observation_start': (datetime.now() - timedelta(days=730)).strftime('%Y-%m-%d')  # Últimos 24 meses
}


response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    observations = data['observations']
 
    if not observations:
        print("Nenhuma observação encontrada.")
        exit()

    filtered_data = [obs for obs in observations]
    
    if not filtered_data:
        print("Nenhum dado encontrado nos últimos 12 meses.")
        exit()
    
    dates = [obs['date'] for obs in filtered_data]
    print(f"Dias filtrados: {dates}") 
    
    values = [float(obs['value']) for obs in filtered_data if obs['value'] != '.']
    print(f"Valores filtrados: {values}") 

    if not values:
        print("Nenhum valor válido encontrado.")
        exit()

    dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o')
    plt.xlabel("Meses")
    plt.ylabel("CPI (Índice de Preços ao Consumidor)")
    plt.title("Inflação no Brasil nos Últimos 12 Meses")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout() 
    plt.show()
else:
    print(f"Erro na requisição: {response.status_code}")

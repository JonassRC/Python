import requests

def listar_criptos():

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&per_page=51'

    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
       
        dados_ordenados = sorted(dados, key=lambda x: x['current_price'], reverse=True)
        
        print("As 50 criptomoedas com maior valor de mercado são:")
       
        for i, cripto in enumerate(dados_ordenados, start=1):
            if 'e' not in str(cripto['current_price']):
                print(f"{i}. {cripto['name']} ({cripto['symbol'].upper()}): R${cripto['current_price']}")
    else:
        print("Erro ao recuperar dados da API.")

listar_criptos()
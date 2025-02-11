import requests

# URL base da API
BASE_URL = "https://olinda.bcb.gov.br/olinda/servico/SICOR/versao/v2/odata/CusteioInvestimentoComercialIndustrialSemFiltros"

def get_dados_credito_rural():
    """
    Faz uma requisição à API e retorna os dados em formato JSON.
    """
    parametros = {
        "$top": 100,    # Número máximo de registros
        "$format": "json"  # Formato de retorno JSON
    }

    resposta = requests.get(BASE_URL, params=parametros)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        print(f"Erro na requisição: {resposta.status_code}")
        return None

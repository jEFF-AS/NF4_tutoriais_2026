import requests

IPEA_BASE_URL = "http://ipeadata.gov.br/api/odata4"

def buscar_serie(codigo):

    url = f"{IPEA_BASE_URL}/ValoresSerie(SERCODIGO='{codigo}')"

    response = requests.get(url)

    data = response.json()

    return {
        "codigo": codigo,
        "dados": data.get("value", [])[:5]
    }

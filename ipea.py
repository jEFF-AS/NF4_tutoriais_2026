import requests

url = "http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='BM12_TJOVER12')"

r = requests.get(url)
data = r.json()

print(data)

#%%
import requests
import json
import logging
#%%
url = "https://economia.awesomeapi.com.br/last/USD-BRL"
ret = requests.get(url)
print(ret)
#%%
dolar = (json.loads(ret.text))['USDBRL']
#%%
print(dolar['bid'])
print(f" 20 dólares hoje custam {float(dolar['bid']) * 20}reais")
# %%
def cotacao(valor, moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace("-","")]
    print(
        f"{valor} {moeda[:3]} correspondem a {float(dolar['bid']) * valor} {moeda[4:]}"
        )

#%%
cotacao(20,"JPY-BRL")

# %%
lst_money = [
    "USD-BRL",
    "EUR-BRL",
    "JPY-BRL"

]
valor = 20 

for moeda in lst_money:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace("-","")]
    print(
        f"{valor} {moeda[:3]} correspondem a {float(dolar['bid']) * valor} {moeda[4:]}"
        )

# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formattter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
ch = logging.StreamHandler()
ch.setFormatter(formattter)
log.addHandler

#%%
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd

#%%
url = "https://portalcafebrasil.com.br/todos/podcasts/"
ret = requests.get(url)

#%%
ret.text

#%%
soup = bs(ret.text)
# %%
soup.find("h5").text
# %%
soup.find("h5").a["href"]
# %%
podcasts = soup.find_all("h5")

# %%
for podcast in podcasts:
    print(f"{podcast.text} - Link: {podcast.a['href']}")
# %%
url = "https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true"
# %%
url.format(5)
# %%
def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')
# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formattter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
ch = logging.StreamHandler()
ch.setFormatter(formattter)
log.addHandler

# %%
i = 1
lst_podcast = []
lst_get = get_podcast(url.format(i))

log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(i)}")
while len(lst_get) > 0:
    lst_podcast = lst_podcast + lst_get
    i += 1
    lst_get = get_podcast(url.format(i))
    log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(i)}")


# %%
lst_podcast
# %%
df = pd.DataFrame(columns=['nome', 'link'])

for podcast in lst_podcast:
    df.loc[df.shape[0]] = [podcast.text, podcast.a['href']]
# %%
df.shape
# %%
df.to_csv("banco_de_podcast.csv", sep=';', index=False)
# %%
df
# %%

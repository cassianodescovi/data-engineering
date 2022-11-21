#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
#%%
driver = webdriver.Chrome('Selenium/src/chromedriver')
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
#%%
table = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]')
driver.close()
# %%
print(table)
# %%
df = pd.read_html('<table>' + table.get_attribute('innerHTML') + '<table>')[0]
# %%
df.to_csv('Nicolas_Cage_movies.csv', sep=';', index=False)
# %%

#%%
from threading import local
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
# %%
cep = sys.argv[1]

if cep:
    driver = webdriver.Chrome('Selenium/src/chromedriver')
    # %%
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
    #%%
    elem_cep = driver.find_element(By.NAME, 'endereco')
    # %%
    elem_cep.clear()
    #%%
    elem_cep.send_keys('80420130')
    # %%
    elem_cmb = driver.find_element(By.NAME, 'tipoCEP')
    elem_cmb.click()
    driver.find_element(By.XPATH, '//*[@id="tipoCEP"]/optgroup/option[6]').click()
    #%%
    driver.find_element(By.ID, 'btn_pesquisar').click()
    # %%
    logradouro = driver.find_element(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]').text
    bairro = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    localidade = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text

    driver.close()
    # %%
    print("""
    Para o Cep {} temos:
    
    Endereço: {}
    Bairro: {}
    Localidade: {}
    """.format(
        cep,
        logradouro.split(' - ')[0],
        bairro,
        localidade
    )
    )
    # %%

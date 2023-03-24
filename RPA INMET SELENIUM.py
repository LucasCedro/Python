#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
from datetime import date, timedelta, datetime, time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import pandas as pd
#----------- esses aqui em baixo podem ser usados com melhor performance ----------
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[2]:


# definindo o nome do arquivo a ser baixado
file_name = 'generatedBy_react-csv.csv'

# definindo o diretório de download
download_dir = "C:\\Python\\"


# In[3]:


# Define o dia de ontem como ultimo dia a ter informações coletadas
yesterday = date.today() - timedelta(days=1)

# formatar a data como string no formato "dd/mm/yyyy"
yesterday_str = yesterday.strftime('%d/%m/%Y')


# In[4]:


#Carrega a base de dados atual
df1 = pd.read_excel('C:\\Python\\Base_Temperatura.xlsx')


# In[5]:


# obter a data da última medição, ou seja, a primeira data a ser buscada no RPA
primeira_data = df1.iloc[df1.shape[0] - 1]["DT_MEDICAO"]
primeira_data = datetime.strptime(primeira_data, '%Y-%m-%d')
primeira_data = primeira_data.strftime('%d/%m/%Y')


# In[6]:


if primeira_data == yesterday_str:
    print("A última data é igual a yesterday")
    sys.exit()


# In[ ]:


# inicia o driver do Chrome com drive atualizado
servico = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument('--headless')
#chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

browser = webdriver.Chrome(service=servico, options=chrome_options)


# In[ ]:


# acessa a página
browser.get('https://tempo.inmet.gov.br/TabelaEstacoes/A756')


# In[ ]:


# espera a página ser carregada
time.sleep(3)


# In[ ]:


#Abre o menu clicando no botão
browser.find_element('xpath', '//*[@id="root"]/div[1]/div[1]/i').click()
time.sleep(1)


# In[ ]:


# preenche o campo de estação
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[3]/i').click()
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[3]/input').send_keys('AGUA CLARA (A756)')


# In[ ]:


# Preenche a Data de Inicio
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[4]/input').click()
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[4]/input').clear()
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[4]/input').send_keys('09/03/2023')
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[4]/input').send_keys(Keys.ENTER)


# In[ ]:


# Preenche a Data Fim
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[5]/input').click()
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[5]/input').clear()
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[5]/input').send_keys(yesterday_str)
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/div[5]/input').send_keys(Keys.ENTER)


# In[ ]:


# espera a página ser carregada
time.sleep(1)


# In[ ]:


# Clica no botão "Gerar Tabela"
browser.find_element('xpath', '//*[@id="root"]/div[2]/div[1]/div[2]/button').click()


# In[ ]:


# espera a tabela carregar
#time.sleep(5)

# tempo máximo que o loop irá esperar pelo elemento em segundos
tempo_maximo = 60

while tempo_maximo > 0:
    try:
        # Tenta encontrar o elemento com o xpath especificado
        elemento = WebDriverWait(browser, 1).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div/span/a'))
        )
        # Se encontrou o elemento, clica no botão e sai do loop
        elemento.click()
        break
    except:
        # Se o elemento ainda não está visível na página, espera mais 1 segundo
        tempo_maximo -= 1
        time.sleep(1)


# In[ ]:


# esperando o arquivo ser baixado
while not os.path.exists(download_dir + file_name):
    time.sleep(1)


# In[ ]:


# renomeando o arquivo
new_file_name = 'dados_inmet.csv'
os.rename(download_dir + file_name, download_dir + new_file_name)


# In[ ]:


# fecha o driver
browser.quit()


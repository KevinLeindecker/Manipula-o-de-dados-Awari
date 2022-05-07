## importações

from selenium import webdriver
from time import sleep
import pandas as pd

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## acessando o browser

URL_IMOVEIS = "https://www.vivareal.com.br/aluguel/rio-grande-do-sul/caxias-do-sul/apartamento_residencial/#tipos=apartamento_residencial,casa_residencial/"

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get(URL_IMOVEIS)

## acessando as informações da URL

resultados_imoveis = driver.find_elements_by_class_name('property-card__main-info')

len(resultados_imoveis)

## acessando as janelas

wait = WebDriverWait(driver, 10)

original_window = driver.current_window_handle

## variáveis para Loop e Loop (clicando nos links da página inicial)

metragem = []
quartos = []
banheiros = []
vagas = []
aluguel = []
tipo = []

while True:
    # For para coleta de descrições
    for res in resultados_imoveis:
        
        assert len(driver.window_handles) == 1
        
        try:
        
            res.click() # Clicar na Descrição

            sleep(3)
            
            wait.until(EC.number_of_windows_to_be(2))
            
        except:
            
            pass
        
        for window_handle in driver.window_handles:
            
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                
                # Obtendo as variáveis selecionadas no site de acordo com a classe
            
                m = driver.find_element_by_class_name('features__item--area')
                q = driver.find_element_by_class_name('features__item--bedroom')
                b = driver.find_element_by_class_name('features__item--bathroom')
                v = driver.find_element_by_class_name('features__item--parking')
                a = driver.find_element_by_class_name('price__price-info')
                t = driver.find_element_by_class_name('price__title')
                
                # Quardando as info nas Listas
                
                metragem.append(m.text)
                quartos.append(q.text)
                banheiros.append(b.text)
                vagas.append(v.text)
                aluguel.append(a.text)
                tipo.append(t.text)
                
                driver.close()
                
                driver.switch_to.window(original_window)
                
                break
                
    break

## criação do dataframe

len(metragem) # a coleta propocia a busca de 35 resultados por vez

## Dicionario

dicionario = {'Metragem': metragem , 'Quartos': quartos, 'Banheiros': banheiros, 'Vagas': vagas, 'Aluguel': aluguel, 'Tipo': tipo}
dados_aluguel_CXS = pd.DataFrame(dicionario)

## visualizando os dados
dados_aluguel_CXS

# Salvando Arquivo em CSV
dados_aluguel_CXS.to_csv('Dados_Aluguel_CXS.csv')
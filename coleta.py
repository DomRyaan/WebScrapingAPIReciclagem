from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
        
class ColetaDados:
    def __init__(self, selenium):
        self.selenium = selenium
        self.distrito_id_dic = {
            'Aquiraz': 1987,
            'Ecocaucaia': 2078,
            'Ecofor': 2069,
            'Ecoosasco': 1988,
            'EcoRondônia': 2081,
            'EcoTaubaté': 2075,
            'Eusébio': 1994,
            'Manaus': 1990,
            'Natal': 2070,
            'Taubaté': 2077
        }
        self.cidades_distrito = {
            'Fortaleza': 'Ecofor',
            'Caucaia': 'Ecocaucaia',
            'Osasco': 'Ecoosasco',
            'Rondonia': 'EcoRondônia',
            'Taubate': 'EcoTaubaté',
            'Eusebio': 'Eusébio',
            'Natal': 'Natal',
            'Taubaté': 'Taubaté'
        }
        
    
    def get_page_selenium(self, url):
        driver = self.selenium.configurar_selenium()
        try:
            driver.get(url)
            WebDriverWait(driver, 15)
            page = driver.page_source
        except TimeoutException:
            print("Tempo esgotado esperando pelos resultados da busca")
            return None
        return BeautifulSoup(page, 'html.parser')


    def get_unidade_value(self, unidade):
        return self.distrito_id_dic.get(unidade)

    def get_cidade_id(self, cidade: str):        
        unidade = self.cidades_distrito.get(cidade)
        if unidade:
            value_unidade = self.get_unidade_value(unidade)  
            if value_unidade:
                return value_unidade
            else:
                raise Exception("Aconteceu um erro")
        else:
            return
            
            
    def get_bairro_id(self, url, value_unidade, bairro: str):
        bairro_upper = bairro.upper()
        page = self.get_page_selenium(url + '/cidade/' + str(value_unidade))
        bairros = page.find('select', {'name': 'bairro'}).find_all('option')
        bairro_user = []
        for opcao in bairros:
            if bairro_upper in opcao.get_text():
                bairro_user.append(opcao)
        if len(bairro_user) > 0:
            id = str(bairro_user[0]).split('\"')                                

            return id[1]
        else:
            raise Exception(f"O bairro {bairro} não foi encontrado!")
        
    def get_json_coletas(self, url):
        page = self.get_page_selenium(url)
        scripts_page = page.find('script').get_text()
        scripts_page_formatado = scripts_page.split("{")
        return scripts_page_formatado[1].split('}')[0]

    def construir_url(self, url, cidade_id, bairro_id):
        return url + '/cidade/' + str(cidade_id) + '/bairro/' + str(bairro_id)

    def made_dict(self, arquivo_json_string: str):
        dicionario_json = {}
        json_string_completo = "{" + arquivo_json_string + "}"
        
        try:
            dicionario_json = json.loads(json_string_completo)
            return dicionario_json
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            print(f"String JSON tentada: {json_string_completo}")
            raise

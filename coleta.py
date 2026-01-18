from constante import DISTRITOS_ID, CIDADE_DISTRITO
import json
import re
from bs4 import BeautifulSoup
from typing import Optional, Dict

class ColetaDados:
    def __init__(self):
        pass

    def _string_to_bs4(self, html_content: str) -> BeautifulSoup:
        """Helper interno para converter string em objeto BeautifulSoup"""
        return BeautifulSoup(html_content, 'html.parser')

    def get_cidade_id(self, cidade: str) -> Optional[int]:
        """Busca o ID da cidade de forma segura"""
        cidade_upper = cidade.upper()
        unidade_nome = CIDADE_DISTRITO.get(cidade_upper)
        
        if not unidade_nome:
            return None
            
        return DISTRITOS_ID.get(unidade_nome)

    def get_bairro_id(self, html_content: str, nome_bairro: str) -> Optional[str]:
        """
        Recebe o HTML da página, procura o select de bairros e retorna o ID do bairro buscado.
        """
        soup = self._string_to_bs4(html_content)
        nome_bairro_upper = nome_bairro.upper()
        
        select_bairro = soup.find('select', {'name': 'bairro'})
        
        if not select_bairro:
            return None

        for option in select_bairro.find_all('option'):
            texto_opcao = option.get_text().upper()
            
            if nome_bairro_upper in texto_opcao:
                # Retorna o valor do atributo 'value' do option correspondente. Mais seguro.
                return option.get('value')
        
        return None

    def extrair_json_coletas(self, html_content: str) -> Dict:
        """
        Extrai o JSON que está escondido dentro de uma tag <script> na página.
        """
        soup = self._string_to_bs4(html_content)
        
        scripts = soup.find_all('script')
        

        target_script = None
        for script in scripts:
            if script.string and "coletas" in script.string: 
                target_script = script.string
                break
        
        if not target_script:
            raise ValueError("Script de dados não encontrado na página.")

        # Regex para extrair apenas o objeto JSON
        match = re.search(r'(\[.*?\]|\{.*?\})', target_script, re.DOTALL)
        
        if match:
            json_str = match.group(1)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass

        raise ValueError("Não foi possível decodificar o JSON do script.")

    def construir_url(self, base_url: str, cidade_id: int, bairro_id: str) -> str:
        return f"{base_url}/cidade/{cidade_id}/bairro/{bairro_id}"
from httpx import AsyncClient, HTTPStatusError, RequestError
from fastapi import HTTPException


" Classe para realizar requisições HTTP assíncronas "
class AsyncCustomRequest:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
            }

    async def get_page(self, url: str):
        """ Função para fazer requisição da página alvo (Marquise Ambiental)

        Args:
            url (str): URL da página

        Raises:
            HTTPStatusError: Capturar erros de status HTTP (404, 500)
            RequestError: Capturar erros de conexão (DNS, Timeout)

        """
        print(f"Fazendo requisição para a URL: {url}")
        async with AsyncClient() as cliente:
            try: 
                response = await cliente.get(url, headers=self.headers, timeout=10.0)
                response.raise_for_status() # Lança HTTPStatusError para códigos de status de erro
            
                return response.text
            
            except HTTPStatusError as e:
                raise HTTPException(status_code=e.response.status_code, detail=f"Erro ao acessar o site: {e}")
            
            except RequestError as e:
                raise HTTPException(status_code=500, detail=f"Falha na conexão: {e}")
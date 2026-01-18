from fastapi import FastAPI, HTTPException
from coleta import ColetaDados
from requeste import AsyncCustomRequest

app = FastAPI()

request_client = AsyncCustomRequest()
parser = ColetaDados()

URL_BASE = "https://marquiseambiental.com.br/marquise_coleta_new"

@app.get("/coletas/{cidade}/{bairro}")
async def get_coletas(cidade: str, bairro: str):    
    
    cidade_id = parser.get_cidade_id(cidade)
    
    if not cidade_id:
        raise HTTPException(status_code=404, detail=f"Cidade '{cidade}' não encontrada.")

    try:
        url_busca_bairro = f"{URL_BASE}/cidade/{cidade_id}"
        html_cidade = await request_client.get_page(url_busca_bairro)
                
        bairro_id = parser.get_bairro_id(html_cidade, bairro)

        if not bairro_id:
             raise HTTPException(status_code=404, detail=f"Bairro '{bairro}' não encontrado nesta cidade.")

        url_final = parser.construir_url(URL_BASE, cidade_id, bairro_id)
        html_final = await request_client.get_page(url_final)
        
        dados_dict = parser.extrair_json_coletas(html_final)
        
        return dados_dict

    except HTTPException:
        raise 
    except Exception as e:
        print(f"Erro interno: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao processar dados da Marquise.")
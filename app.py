from flask import Flask, jsonify
from selenium_classe import Selenium
from coleta import ColetaDados

app = Flask(__name__)
URL = "https://marquiseambiental.com.br/marquise_coleta_new"

@app.route('/coletas/<cidade>/<bairro>', methods=['GET'])
def get_coletas(cidade, bairro):
    selenium = Selenium()
    coleta_dados = ColetaDados(selenium=selenium)
    
    pagina = coleta_dados.get_page_selenium(URL)
    value_unidade = coleta_dados.get_cidade_id(cidade)
    print("Valor da unidade obtido: ", value_unidade)
    if not value_unidade:
        return jsonify({"error": f"Cidade {cidade} não encontrada."}), 404
    
    if value_unidade:
        value_bairro = coleta_dados.get_bairro_id(URL, value_unidade, bairro)
        
        url_coleta = coleta_dados.construir_url(URL, value_unidade, value_bairro)
        json_coletas_string = coleta_dados.get_json_coletas(url_coleta)
        
        json_coletas_dict = coleta_dados.made_dict(json_coletas_string)
        return jsonify(json_coletas_dict)

if __name__ == '__main__':
    app.run()
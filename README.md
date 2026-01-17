# ColetaAPI - API de Web Scraping para Coleta de Reciclagem

## Descrição

A **ColetaAPI** é uma API REST desenvolvida em Flask que utiliza técnicas de web scraping para coletar dados de agendamento de coleta de reciclagem do site da Marquise Ambiental. A API permite consultar horários e informações de coleta de lixo reciclável para diversas cidades e bairros suportados.

## Funcionalidades

- **Consulta de Coletas**: Obtenha dados de coleta de reciclagem por cidade e bairro
- **Web Scraping Automatizado**: Utiliza Selenium para navegação headless no site
- **Resposta em JSON**: Retorna dados estruturados em formato JSON
- **Suporte a Múltiplas Cidades**: Atualmente suporta cidades como Fortaleza, Caucaia, Osasco, entre outras

## Cidades Suportadas

- Fortaleza (Ecofor)
- Caucaia (Ecocaucaia)
- Osasco (Ecoosasco)
- Rondônia (EcoRondônia)
- Taubaté (EcoTaubaté)
- Eusébio
- Natal
- Manaus (não mapeado)
- Aquiraz (não mapeado)

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado (para Selenium)
- ChromeDriver (gerenciado automaticamente pelo Selenium)

### Passos de Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd ColetaAPI
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   python app.py
   ```

A API estará disponível em `http://localhost:5000`

## Uso

### Endpoint Principal

```
GET /coletas/<cidade>/<bairro>
```

#### Parâmetros

- `cidade`: Nome da cidade (ex: Fortaleza, Caucaia, Osasco)
- `bairro`: Nome do bairro (case insensitive, busca parcial)

#### Exemplo de Requisição

```bash
curl "http://localhost:5000/coletas/Fortaleza/Centro"
```

#### Exemplo de Resposta

```json
{
  "dados": {
    "coleta": "Segunda-feira",
    "horario": "08:00 - 12:00",
    "tipo": "Recicláveis"
  }
}
```

#### Respostas de Erro

- `404`: Cidade ou bairro não encontrado
- `500`: Erro interno do servidor

## Estrutura do Projeto

```
ColetaAPI/
├── app.py              # Aplicação Flask principal
├── coleta.py           # Lógica de coleta de dados
├── selenium.py         # Configuração do Selenium
├── README.md           # Este arquivo
└── requirements.txt    # Dependências Python
```

## Dependências

- **Flask**: Framework web para a API
- **Selenium**: Automação de navegador para web scraping
- **BeautifulSoup4**: Parsing de HTML
- **Chrome WebDriver**: Driver para navegação headless

## Desenvolvimento

### Executando em Modo de Desenvolvimento

```bash
export FLASK_ENV=development
python app.py
```

### Testes

Para testar a API, você pode usar ferramentas como Postman, curl ou qualquer cliente HTTP.

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## Avisos

- Esta API realiza web scraping em sites de terceiros. Use com responsabilidade e respeite os termos de serviço dos sites.
- O scraping pode ser afetado por mudanças no layout ou estrutura dos sites alvo.
- Recomenda-se implementar cache para evitar sobrecarga nos servidores externos.

## Suporte

Para dúvidas ou problemas, abra uma issue no repositório do projeto.


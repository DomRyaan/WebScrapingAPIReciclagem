# ColetaAPI - API de Web Scraping para Coleta de Reciclagem

## Descrição

A **ColetaAPI** é uma API REST desenvolvida em FastAPI que utiliza técnicas de web scraping para coletar dados de agendamento de coleta de reciclagem do site da Marquise Ambiental. A API permite consultar horários e informações de coleta de lixo reciclável para diversas cidades e bairros suportados, utilizando requisições HTTP assíncronas com httpx para maior velocidade e eficiência.

## Funcionalidades

- **Consulta de Coletas**: Obtenha dados de coleta de reciclagem por cidade e bairro
- **Web Scraping Automatizado**: Utiliza httpx para requisições HTTP assíncronas
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
   python main.py
   ```

A API estará disponível em `http://localhost:8000`

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
curl "http://localhost:8000/coletas/Fortaleza/Centro"
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
├── main.py             # Aplicação FastAPI principal
├── coleta.py           # Lógica de coleta de dados
├── requeste.py         # Cliente HTTP assíncrono para requisições
├── constante.py        # Constantes e mapeamentos de cidades/distritos
├── README.md           # Este arquivo
└── requirements.txt    # Dependências Python
```

## Dependências

- **FastAPI**: Framework web moderno e rápido para APIs
- **Uvicorn**: Servidor ASGI para FastAPI
- **httpx**: Cliente HTTP assíncrono para Python
- **BeautifulSoup4**: Parsing de HTML

## Desenvolvimento

### Executando em Modo de Desenvolvimento

```bash
fastapi dev main.py
```

### Documentação da API

A documentação interativa da API está disponível em `http://localhost:8000/docs` (Swagger UI) ou `http://localhost:8000/redoc` (ReDoc).

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


# Atividade: Análise de uma API REST

## Objetivo

Nesta atividade, você irá analisar uma API REST pública para identificar como ela organiza seus recursos, quais métodos HTTP utiliza e como o cliente envia estado para o servidor.

---

## Instruções

1. Faça um fork deste repositório para sua conta no GitHub.
2. Escolha uma API REST pública e gratuita.
3. Analise a API.
4. Documente suas conclusões em um arquivo `README.md`.
5. Faça commit e envie suas alterações para o seu fork.
6. Entregue o link do seu repositório.

---

## O que deve ser analisado

### 1. Recursos

Identifique os principais recursos da API.

Exemplos:

* `usuarios`
* `produtos`
* `estados`
* `municipios`

### 2. Métodos HTTP

Liste os métodos HTTP disponíveis para os recursos analisados.

Exemplos:

* `GET`
* `POST`
* `PUT`
* `PATCH`
* `DELETE`

### 3. Estado enviado pelo cliente

Explique quais informações o cliente envia para o servidor, por exemplo:

* Parâmetros na URL
* Query parameters
* Corpo da requisição (JSON)
* Cabeçalhos HTTP
* Tokens de autenticação

### 6. Exemplo de uso com `curl`

Inclua pelo menos três exemplos de requisição usando `curl` e suas respostas, assim como cabeçalhos de pacotes http e uma discussão breve.

---

## Estrutura sugerida do `README.md`

````markdown
# Análise da API X

## API escolhida
Nome da API e link para a documentação oficial.

## Recursos
- Recurso 1
- Recurso 2
- Recurso 3

## Métodos HTTP
- GET
- POST

## Estado enviado pelo cliente
Descrição dos parâmetros, headers e corpo da requisição.

## Exemplo com curl
```bash
curl https://api.exemplo.com/recurso
````

## Outras formas de organizar os recursos (opcional)

Discussão sobre possíveis alternativas.

## Escalabilidade horizontal (opcional)

Discussão sobre cache, balanceamento e outras estratégias.

```

---

## APIs sugeridas

- IBGE — https://servicodados.ibge.gov.br/api/docs
- IPEA Data — https://www.ipea.gov.br
- Open-Meteo — https://open-meteo.com
- PokéAPI — https://pokeapi.co
- SpaceX API — https://github.com/r-spacex/SpaceX-API
- TMDb — https://developer.themoviedb.org
- World Bank API — https://api.worldbank.org

---



## Dicas

- Consulte a documentação oficial da API.
- Teste as requisições com `curl`, Postman ou Insomnia.
- Prefira APIs públicas e bem documentadas.
- Seja objetivo, mas explique suas decisões.

---

## Entrega

Envie o link do seu repositório forkado (se públicO) contendo o `README.md` com a análise completa.
Caso o repositório esteja privado, envie a resposta em formato markdown para luisvinicius.professor@uniatenas.edu.br
```

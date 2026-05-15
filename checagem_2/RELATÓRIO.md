# Análise da API X

## API escolhida
PokéAPI: 
```bash
https://pokeapi.co/docs/v2
```

## Recursos
```bash
https://pokeapi.co/api/v2/berry/{id or name}/
https://pokeapi.co/api/v2/encounter-method/{id or name}/
https://pokeapi.co/api/v2/location/{id or name}/
```

## Métodos HTTP
- GET: É o único método HTTP suportado. Ao tentar usar POST, PUT, ou DELETE, o servidor rejeitará a requisição (geralmente retornando um erro 404 Not Found ou 405 Method Not Allowed), pois não é permitido alterar o banco de dados deles.

## Estado enviado pelo cliente
Parâmetros na URL (Path Parameters): /berry/Cheri; /berry-firmness/2/; /pokemon/25.
Query parameters (Paginação): ?limit=10&offset=5 (traz 5 resultados, pulando os 10 primeiros)

## Exemplo com curl
Exemplo 1: Buscar dados de um Pokémon específico pelo nome:
```bash
curl -X GET https://pokeapi.co/api/v2/pokemon/charizard
```
Exemplo 2: Buscar a lista de Pokémon usando paginação (trazendo 10 itens):
```bash
curl -X GET "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"

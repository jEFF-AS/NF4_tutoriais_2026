# API IPEA - Atividade Avaliativa

Curso: Sistemas de Informação
Disciplina: Integração e Consumo de APIs
Professor: Me. Luis Vinicius Costa Silva
Turma: Noturno – 1º Semestre 2026

---

# Sobre o Projeto

Este é um projeto base de uma API simples desenvolvida em Flask para consulta de dados econômicos utilizando a API pública do IPEA.

O projeto já possui:

* Estrutura básica em camadas
* Controllers
* Services
* Integração inicial com Flask
* Endpoint de health check
* Endpoint de consulta de séries econômicas

No entanto, a aplicação ainda está incompleta e necessita de implementação e melhorias.

---

# Objetivo da Atividade

Completar a API utilizando conceitos estudados em sala relacionados a:

* APIs REST
* Integração de sistemas
* Consumo de APIs externas
* JSON
* Arquitetura simples em camadas
* Fluxo HTTP

Os alunos deverão implementar os endpoints faltantes, corrigir problemas e fazer a aplicação funcionar corretamente.

---

# Estrutura do Projeto

```text
api-ipea/
│
├── app.py
├── requirements.txt
│
├── controllers/
│   ├── health_controller.py
│   └── serie_controller.py
│
└── services/
    └── ipea_service.py
```

---

# Como Executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

---

# Endpoints Esperados

## Health Check

```text
GET /health
```

Exemplo:

```bash
curl http://localhost:5000/health
```

Resposta esperada:

```json
{
  "status": "online"
}
```

---

## Consulta de Série Econômica

```text
GET /serie/<codigo>
```

Exemplo:

```bash
curl http://localhost:5000/serie/BM12_TJOVER12
```

---

# Exemplos de Séries do IPEA

SELIC:

```text
BM12_TJOVER12
```

IPCA:

```text
PRECOS12_IPCAG12
```

PIB:

```text
GM366_NGDPFCN366
```

---

# O que Deve Ser Implementado

Os alunos deverão:

* registrar corretamente as rotas no Flask
* implementar os controllers
* implementar o service de integração com o IPEA
* consumir a API externa utilizando requests
* retornar JSON válido
* testar os endpoints com curl
* tratar possíveis erros básicos

---

# Parte Teórica

Criar um arquivo chamado:

```text
RELATORIO.md
```

e responder:

a) O que é uma API REST e como ela funciona?

b) Qual a importância da integração entre sistemas utilizando APIs?

c) Explique o fluxo da requisição desde o curl até a API externa do IPEA.

d) Explique a diferença entre controller e service na arquitetura utilizada.

e) Desenhe um diagrama de sequência representando:

```text
Cliente -> Flask -> Controller -> Service -> API IPEA
```

---

# Exemplos de curl

Funcionando:

```bash
curl http://localhost:5000/health
```

```bash
curl http://localhost:5000/serie/BM12_TJOVER12
```

Endpoints não implementados:

```bash
curl http://localhost:5000/report
```

```bash
curl http://localhost:5000/stats
```

---

# Entrega

Todos os alunos deverão:

* subir o código em um repositório público no GitHub

OU

* enviar um arquivo .zip contendo o projeto completo por e-mail

E-mail para envio:

```text
luisvinicius.professor@uniatenas.edu.br
```

O projeto deve conter:

* código-fonte
* RELATORIO.md
* endpoints funcionando

---

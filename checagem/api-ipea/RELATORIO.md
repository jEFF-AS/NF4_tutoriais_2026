# RELATÓRIO: Integração e Consumo de APIs (IPEA)

**Curso:** Sistemas de Informação
**Disciplina:** NF4: Integração e Consumo de APIs

---

### a) O que é uma API REST e como ela funciona?

**API REST** (*Representational State Transfer*) é um estilo de arquitetura de software que define um conjunto de regras e padrões para a criação de *web services*. Ela funciona como uma interface padronizada que permite que diferentes aplicações se comuniquem pela internet utilizando o protocolo HTTP.

**Como funciona:**
* **Comunicação Cliente-Servidor:** O cliente (terminal, navegador, app) faz uma requisição, e o servidor processa e devolve uma resposta.
* **Métodos HTTP:** Utiliza os verbos padrão da web para indicar a ação desejada: `GET` (buscar dados), `POST` (enviar/criar), `PUT` (atualizar) e `DELETE` (remover).
* **Stateless (Sem estado):** O servidor não guarda o histórico ou o estado das requisições do cliente. Cada chamada é independente e deve conter todas as informações necessárias para ser processada.
* **Formato de Dados:** As informações geralmente trafegam no formato **JSON** (*JavaScript Object Notation*), que é leve e de fácil leitura para humanos e máquinas.

---

### b) Qual a importância da integração entre sistemas utilizando APIs?

A integração via APIs é fundamental no desenvolvimento de software moderno pelos seguintes motivos:
* **Reaproveitamento e Eficiência:** Evita o retrabalho. Em vez de criar e manter um banco de dados econômico complexo, o sistema simplesmente consome a API do IPEA, que já fornece os dados atualizados.
* **Interoperabilidade:** Permite que sistemas desenvolvidos em linguagens e plataformas totalmente diferentes (ex: um *backend* em Python se comunicando com um servidor legado em Java) troquem dados de forma transparente.
* **Desacoplamento e Escalabilidade:** Facilita arquiteturas baseadas em microsserviços. O sistema principal e as integrações funcionam de forma independente, tornando a aplicação mais fácil de manter e escalar.

---

### c) Explique o fluxo da requisição desde o curl até a API externa do IPEA.

O fluxo de comunicação ocorre no seguinte ciclo de requisição e resposta:

1. **Cliente (`curl`):** O usuário executa a chamada `curl http://localhost:5000/serie/BM12_TJOVER12`, gerando uma requisição HTTP `GET`.
2. **Roteamento (Flask):** O servidor Flask local recebe a requisição na porta 5000, lê a URL e identifica que a rota `/serie/<codigo>` deve acionar o controlador correspondente.
3. **Controller (`serie_controller`):** O controlador recebe o parâmetro da URL (`BM12_TJOVER12`) e atua como intermediário, chamando a camada de serviço e passando esse código.
4. **Service (`ipea_service`):** O serviço concentra a regra de integração. Ele monta a URL OData oficial do IPEA e utiliza a biblioteca `requests` para disparar uma nova requisição HTTP, desta vez externa, para os servidores do governo.
5. **API IPEA:** O servidor remoto processa a requisição, consulta o banco de dados e devolve os valores da série em formato JSON.
6. **Resposta:** O `service` recebe o JSON do IPEA e o devolve ao `controller`. O `controller` formata os dados usando `jsonify` e o Flask empacota a resposta HTTP (Status 200), entregando-a de volta ao terminal do cliente.

---

### d) Explique a diferença entre controller e service na arquitetura utilizada.

A arquitetura em camadas separa as responsabilidades (*Separation of Concerns*) para manter o código organizado:

* **Controller (Camada de Apresentação/Rotas):** É responsável apenas por lidar com requisições e respostas HTTP. Ele extrai dados da URL, chama os serviços necessários e retorna a resposta formatada (ex: `jsonify`) com o *Status Code* adequado. Não deve conter lógica de negócios.
* **Service (Camada de Negócios):** É onde a lógica real da aplicação reside. O serviço não sabe de onde a requisição veio (se foi via web, terminal, etc.). Sua responsabilidade é processar regras, formatar dados, fazer cálculos e, neste caso, realizar a comunicação direta com APIs externas utilizando o `requests`.

---

### e) Diagrama de Sequência: Cliente -> Flask -> Controller -> Service -> API IPEA

sequenceDiagram
    participant Cliente
    participant Flask
    participant Service
    participant API_IPEA

    Cliente->>Flask: GET /health
    Flask-->>Cliente: JSON resposta

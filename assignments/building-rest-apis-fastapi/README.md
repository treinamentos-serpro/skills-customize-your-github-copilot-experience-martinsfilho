# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definindo rotas, validando dados de entrada e implementando operações CRUD. Você também praticará métodos HTTP, códigos de status e respostas para recursos inexistentes.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Complete o código inicial para configurar uma aplicação FastAPI e criar rotas básicas para apresentar e verificar a disponibilidade da API.

#### Requirements
O programa concluído deve:

- Criar uma instância `FastAPI` chamada `app`.
- Implementar `GET /` com uma resposta JSON que identifique a API.
- Implementar `GET /health` com uma resposta JSON indicando que o serviço está ativo.
- Iniciar localmente com `uvicorn starter-code:app --reload` após instalar as dependências com `pip install "fastapi[standard]"`.

### 🛠️ Add Item Read Endpoints

#### Description
Crie um recurso `Item` e implemente endpoints para consultar os itens armazenados em memória. Cada item deve ter um identificador, nome, descrição e preço.

#### Requirements
O programa concluído deve:

- Definir um modelo Pydantic para os dados de um item, validando nome, descrição e preço.
- Implementar `GET /items` para retornar todos os itens.
- Implementar `GET /items/{item_id}` para retornar um item pelo identificador.
- Responder com o código HTTP `404` quando o identificador solicitado não existir.

### 🛠️ Implement Item CRUD Operations

#### Description
Complete a API para que clientes possam criar, atualizar e remover itens, além de consultá-los.

#### Requirements
O programa concluído deve:

- Implementar `POST /items` para criar um item, atribuir um identificador único e responder com o código HTTP `201`.
- Implementar `PUT /items/{item_id}` para substituir os dados de um item existente.
- Implementar `DELETE /items/{item_id}` para remover um item existente e responder com o código HTTP `204`.
- Responder com o código HTTP `404` ao tentar atualizar ou remover um item inexistente.
- Manter as alterações disponíveis enquanto o processo da API estiver em execução.

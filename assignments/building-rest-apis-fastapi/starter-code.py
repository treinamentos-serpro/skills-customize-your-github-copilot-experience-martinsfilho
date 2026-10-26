from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Items API")


class ItemInput(BaseModel):
    name: str
    description: str
    price: float


class Item(ItemInput):
    id: int


items: dict[int, Item] = {}
next_item_id = 1


@app.get("/")
def read_root():
    # TODO: Retorne uma mensagem JSON que identifique a API.
    pass


@app.get("/health")
def read_health():
    # TODO: Retorne uma mensagem JSON indicando que a API está ativa.
    pass


@app.get("/items")
def read_items():
    # TODO: Retorne todos os itens.
    pass


@app.get("/items/{item_id}")
def read_item(item_id: int):
    # TODO: Retorne o item solicitado ou lance HTTPException com status 404.
    pass


@app.post("/items", status_code=201)
def create_item(item_input: ItemInput):
    # TODO: Crie um item, atribua um ID único, armazene-o e retorne-o.
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item_input: ItemInput):
    # TODO: Substitua um item existente ou lance HTTPException com status 404.
    pass


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    # TODO: Remova um item existente ou lance HTTPException com status 404.
    # Uma resposta 204 não deve incluir um corpo.
    pass

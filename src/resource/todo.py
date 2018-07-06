import typing
from apistar import http, types, validators, Route


class Todo(types.Type):
    id = validators.Integer(minimum=1)
    task = validators.String(max_length=100)


def item_get(todo_id: str) -> Todo:
    todo = Todo(id=int(todo_id), task='Buy milk')
    return todo


def item_put(todo_id: str, data: http.RequestData) -> Todo:
    todo = Todo(id=int(todo_id), task=data['task'])
    return todo


def item_delete() -> http.JSONResponse:
    return http.JSONResponse(None, status_code=204)


def collection_get() -> typing.List[Todo]:
    todo = Todo(id=1, task='Buy milk')
    return [todo]


def collection_post(todo: Todo) -> http.JSONResponse:
    return http.JSONResponse(todo, status_code=201)


ROUTES = [
    Route('/{todo_id}', method='GET', handler=item_get),
    Route('/{todo_id}', method='PUT', handler=item_put),
    Route('/{todo_id}', method='DELETE', handler=item_delete),
    Route('/', method='POST', handler=collection_post),
    Route('/', method='GET', handler=collection_get),
]

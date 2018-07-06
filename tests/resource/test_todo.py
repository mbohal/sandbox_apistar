from apistar import test
from app import APP


CLIENT = test.TestClient(APP)

def test_todo_item_get():
    response = CLIENT.get('/todos/1')
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'task': 'Buy milk'}

def test_todo_item_put():
    response = CLIENT.put('/todos/100', {'task': 'Buy butter'})
    assert response.status_code == 200
    assert response.json() == {'id': 100, 'task': 'Buy butter'}

def test_todo_item_delete():
    response = CLIENT.delete('/todos/23')
    assert response.status_code == 204

def test_todo_collection_post():
    response = CLIENT.post('/todos/', json={'id': 2, 'task': 'Buy apples'}, allow_redirects=False)
    assert response.status_code == 201
    assert response.json() == {'id': 2, 'task': 'Buy apples'}

def test_todo_collection_get():
    response = CLIENT.get('/todos')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'task': 'Buy milk'}]

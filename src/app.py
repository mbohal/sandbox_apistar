from resource.todo import ROUTES as TODO_ROUTES
from apistar import App, Include


ROUTES = [
    Include('/todos', name='users', routes=TODO_ROUTES),
]

APP = App(routes=ROUTES)

if __name__ == '__main__':
    APP.serve('127.0.0.1', 5000, debug=True)

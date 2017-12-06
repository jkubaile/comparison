import psycopg2

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import random

conn = psycopg2.connect("dbname=tester user=postgres")


def hello_world(request):
    result = []
    cur = conn.cursor()
    for i in range(100):
        _id = random.randint(1, 11000010)
        cur.execute("SELECT * from towns where id = {};".format(_id))
        result.append(cur.fetchone())
    return result

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello', renderer="json")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()

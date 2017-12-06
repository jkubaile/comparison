import psycopg2
from sanic import Sanic
from sanic import response
import random

conn = psycopg2.connect("dbname=tester user=postgres")

app = Sanic()


@app.route("/")
async def hello(request):
    cur = conn.cursor()
    result = []
    for i in range(100):
        _id = random.randint(1, 11000010)
        cur.execute("SELECT * from towns where id = {};".format(_id))
        result.append(cur.fetchone())

    return response.json(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

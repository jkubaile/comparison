import random
import asyncpg

#import asyncio
#import uvloop

from sanic import Sanic
from sanic.response import json

DB_CONFIG = {
    'host': 'localhost',
    'user': 'postgres',
    'password': None,
    # 'port': '<port>',
    'database': 'tester'
}

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# loop = asyncio.get_event_loop()

app = Sanic(__name__)

@app.listener('before_server_start')
async def register_db(app, loop):
    app.pool = await asyncpg.create_pool(**DB_CONFIG, loop=loop, max_size=100)
#     # async with app.pool.acquire() as connection:
#     #     await connection.execute('DROP TABLE IF EXISTS sanic_post')
#     #     await connection.execute("""CREATE TABLE sanic_post (
#     #                             id serial primary key,
#     #                             content varchar(50),
#     #                             post_date timestamp
#     #                         );""")
#     #     for i in range(0, 1000):
#     #         await connection.execute(f"""INSERT INTO sanic_post
#     #             (id, content, post_date) VALUES ({i}, {i}, now())""")

@app.get('/')
async def root_get(request):
    result = []
    async with app.pool.acquire() as connection:
        for i in range(100):
            _id = random.randint(1, 11000010)
            result.append(await connection.fetch('SELECT * FROM towns where id = {}'.format(_id)))

    return json(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

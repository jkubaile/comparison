import psycopg2

conn = psycopg2.connect("dbname=tester user=postgres")

cur = conn.cursor()

result = cur.execute("SELECT * from towns limit 10")

import pdb; pdb.set_trace()



# tester=# CREATE TABLE Towns (
#   id SERIAL UNIQUE NOT NULL,
#   code VARCHAR(10) NOT NULL, -- not unique
#   article TEXT,
#   name TEXT NOT NULL, -- not unique
#   department VARCHAR(4));

# select
#     left(md5(i::text), 10),
#     md5(random()::text),
#     md5(random()::text),
#     left(md5(random()::text), 4)
# from generate_series(1, 1000000) s(i);

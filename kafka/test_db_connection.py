import psycopg2

conn = psycopg2.connect(
    dbname="livinglabvisualization",
    user="lukasmetzler",
    password="lukasmetzler",
    host="localhost",
    port="5432",
)

cur = conn.cursor()
cur.execute(
    "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
)
print(cur.fetchall())
cur.close()
conn.close()

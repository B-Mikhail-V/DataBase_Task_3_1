import psycopg2
import sqlalchemy
import pandas as pd
# from pandas import openpyxl


# engine = sqlalchemy.create_engine('postgresql://mikhail:123456@localhost:5432/dvdrental')
engine = sqlalchemy.create_engine('postgresql://mikhail:123456@localhost:5432/muzic_2')


connection = engine.connect()

# connection.execute("""
# INSERT INTO singers(name)
# VALUES('Michael Jackson',
# 'Madonna',
# 'Frank Sinatra',
# 'Paul McCartney',
# 'Sting',
# 'Алла Пугачева',
# 'Elton John',
# 'Peter Gabriel');
#
# """)

# connection.execute("""
# INSERT INTO singers(name)
# VALUES ('Michael Jackson'),
# ('Madonna'),
# ('Frank Sinatra'),
# ('Paul McCartney'),
# ('Sting'),
# ('Алла Пугачева'),
# ('Elton John'),
# ('Peter Gabriel')
#
# """)
df = pd.read_excel("For Database_25_01_22.xlsx", sheet_name="List_1")
print(len(df))
conn = connect_to_db(DB_FILE_PATH)
df.to_sql(singers, conn, index=False)

# connection.execute("""
# INSERT INTO singers(name)
# VALUES df
#
# """)


sel = connection.execute("""
SELECT * FROM singers;
""").fetchall()
print(sel)

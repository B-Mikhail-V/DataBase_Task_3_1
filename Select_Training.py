import psycopg2
import sqlalchemy
import pandas as pd
# from pandas import openpyxl


# engine = sqlalchemy.create_engine('postgresql://mikhail:123456@localhost:5432/dvdrental')
from pandas import DataFrame

engine = sqlalchemy.create_engine('postgresql://mikhail:123456@localhost:5432/musik_1')


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
# # """)
table_dict = {}
table_list = ['singers', 'genres', 'albums', 'tracks', 'collections', 'collectionstracks', 'singersalbums', 'singersgenres']
sheets_list = ['List_1', 'List_2', 'List_3', 'List_4', 'List_5', 'List_6', 'List_7', 'List_8']
for i in range(5):

    df: DataFrame = pd.read_excel("For Database_25_01_22.xlsx", sheets_list[i], index_col=0)
    print(df)
    df.to_sql(table_list[i], con=engine, if_exists='append', index=False)

# conn = connect_to_db(DB_FILE_PATH)
# df.to_sql(singers, conn, index=False)




# sel = connection.execute("""
# SELECT * FROM singers;
# """).fetchall()
# print(sel)

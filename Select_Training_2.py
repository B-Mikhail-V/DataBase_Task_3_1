import psycopg2
import sqlalchemy
import pandas as pd
# from pandas import openpyxl


# engine = sqlalchemy.create_engine('postgresql://mikhail:123456@localhost:5432/dvdrental')
from pandas import DataFrame

engine = sqlalchemy.create_engine('postgresql://mikhail:123456@localhost:5432/musik_1')


connection = engine.connect()

# df1: DataFrame = pd.read_excel("For Database_25_01_22.xlsx", 'tables', index_col=False)
# table_list = df1.values.tolist()
# # print(table_list)
#
#
# for i in range(len(table_list)):
#     df: DataFrame = pd.read_excel("For Database_25_01_22.xlsx", table_list[i][0], index_col=0)
#     # print(df)
#     df.to_sql(table_list[i][0], con=engine, if_exists='append', index=False)

sel = connection.execute("""
SELECT * FROM singers;
""").fetchall()
print(sel)

sel_1 = connection.execute("""
SELECT title, recording_year FROM albums
WHERE recording_year = '2019';
""").fetchall()
print(sel_1)

sel_2 = connection.execute("""
SELECT duration, title FROM tracks
WHERE duration = (SELECT MAX(duration) from tracks)
""").fetchall()
print(sel_2)

sel_3 = connection.execute("""
SELECT duration, title FROM tracks
WHERE duration >= 3.5 * 60
""").fetchall()
print(sel_3)

sel_4 = connection.execute("""
SELECT title FROM collections
WHERE recording_year BETWEEN '2018' and '2020'
""").fetchall()
print(sel_4)

sel_5 = connection.execute("""
SELECT name FROM singers
WHERE name NOT LIKE '%% %%'
""").fetchall()
print(sel_5)

sel_6 = connection.execute("""
SELECT title FROM tracks
WHERE title ILIKE '%%My%%'
""").fetchall()
print(sel_6)

import sqlalchemy
import pandas as pd
from pandas import DataFrame

engine = sqlalchemy.create_engine('postgresql://mikhail:123456@localhost:5432/musik_1')

connection = engine.connect()

df1: DataFrame = pd.read_excel("For Database_25_01_22.xlsx", 'tables', index_col=False)
table_list = df1.values.tolist()


for i in range(len(table_list)):
    df: DataFrame = pd.read_excel("For Database_25_01_22.xlsx", table_list[i][0], index_col=0)
    # print(df)
    df.to_sql(table_list[i][0], con=engine, if_exists='append', index=False)
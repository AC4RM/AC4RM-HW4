from solution import *
import sqlite3
import pandas as pd
import requests


def test_python():
    assert expo_list([[1, 2], [2, 3, 4], [5, 6, 7]]) == [[1, 2], [4, 9, 16], [125, 216, 343]]
    assert expo_list([[1, 2, 3], [5, 6], [10, 10]]) == [[1, 2, 3], [25, 36], [1000, 1000]]


def test_sql():
    url = "https://docs.google.com/uc?export=download&id=1BzjCEmvPdi9PZnFGGl7L9N8wSITrrcWf"

    with open('data.db', 'wb') as out_file:
        content = requests.get(url).content
        out_file.write(content)

    con = sqlite3.connect('data.db')  # open a database file

    customer_df_1 = pd.read_sql_query(sql_query_1, con)
    customer_df_2 = pd.read_sql_query(sql_query_2, con)

    assert customer_df_1['address'].shape[0] == 3
    assert customer_df_2['first_name'].to_list() == ['Clemmie', 'Elka', 'Freddi']

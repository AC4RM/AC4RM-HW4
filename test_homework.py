from homework import *
import urllib.request
import sqlite3
import pandas as pd
import sklearn


def test_python():
    assert expo_list([[1, 2], [2, 3, 4], [5, 6, 7]]) == [[1, 2], [4, 9, 16], [125, 216, 343]]
    assert expo_list([[1, 2, 3], [5, 6], [10, 10]]) == [[1, 2, 3], [25, 36], [1000, 1000]]


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')  # open a database file

    customer_df_1 = pd.read_sql_query(sql_query_1, con)
    customer_df_2 = pd.read_sql_query(sql_query_2, con)

    assert customer_df_1['address'].shape[0] == 3
    assert customer_df_2['first_name'].to_list() == ['Clemmie', 'Elka', 'Freddi']


def test_model():
    model, scores = train_model()
    assert isinstance(model, sklearn.neighbors._classification.KNeighborsClassifier)
    assert len(scores) == 20
    assert scores[0] > scores[-1]


def test_regex():
    assert extract_date('Post Date: 05/22/2023') == ['05', '22', '2023']
    assert extract_date('01/01/1970') == ['01', '01', '1970']


def test_monte_carlo():
    results = []
    np.random.seed(42)
    for i in range(50):
        result = simple_bettor_v4(10000, 3000, 200)
        results.append(result)

    assert all([len(x) == 201 for x in results])
    assert sum([x[-1] <= 0 for x in results]) == 34



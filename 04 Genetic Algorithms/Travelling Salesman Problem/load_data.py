import pandas as pd

def load_data():
    df_xy = pd.read_csv("/home/deyan/Desktop/AI/04 Genetic Algorithms/test_data/UK_TSP/uk12_xy.csv", header=None, names=['x','y'])
    df_cityname = pd.read_csv("/home/deyan/Desktop/AI/04 Genetic Algorithms/test_data/UK_TSP/uk12_name.csv", header=None, names=['name'])
    print(list(df_cityname['name']))
    res = []
    for i in range(12):
        res.append((df_cityname['name'][i], (df_xy['x'][i], df_xy['y'][i])))
    return res
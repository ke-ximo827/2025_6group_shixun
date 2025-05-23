import pandas as pd
import os


def analyze():
    path = os.path.dirname(os.getcwd())
    prov_path = os.path.join(path, 'people_analyze', 'spider', 'province.csv')
    data_path = os.path.join(path, 'people_analyze', 'spider', 'map.csv')

    prov_df = pd.read_csv(prov_path)

    df = pd.read_csv(data_path)

    prov_names = list(prov_df['name'])

    grouped_df = df.groupby('pName')

    dataList = []

    for pName in prov_names:
        df1 = grouped_df.get_group(pName)

        # pct_change():计算增长百分比，公式：(当前行-前一行) / 前一行
        s = df1['data'].pct_change() * 100

        data = round(list(s)[1], 2)

        t = (pName, data)

        dataList.append(t)

    return dataList


if __name__ == '__main__':
    analyze()

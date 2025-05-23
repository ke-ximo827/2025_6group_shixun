import pandas as pd
import os


def analyze():
    # 获取数据文件路径
    path = os.path.dirname(os.getcwd())
    file_path = os.path.join(path, 'people_analyze', 'spider', 'yuyeCount.csv')
    print(file_path)

    # 读取数据文件，生成DataFrame
    df = pd.read_csv(file_path)

    # 根据折线图的数据格式将DataFrame拆分为X轴和Y轴数据
    yearList = list(df['year'].astype(str))
    dataList = list(df['data'])

    dic = {'x': yearList, 'y': dataList}

    return dic

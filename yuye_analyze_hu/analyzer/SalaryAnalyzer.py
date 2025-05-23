import pandas as pd
import os

'''
按指定的年份计算每个季度的人均收入
'''


def analyze(year):
    path = os.path.dirname(os.getcwd())
    file_path = os.path.join(path, 'people_analyze', 'spider', 'salary.csv')

    df = pd.read_csv(file_path)

    # groupby():分组
    # 参数：by-按照哪个字段进行分组
    grouped_df = df.groupby('year')

    # get_group():根据分组名获取分组数据
    # 参数：name：获取分组的名称
    df1 = grouped_df.get_group(year)

    # sort_values():根据列名进行排序，默认是按照升序排序
    # 参数：by-列名
    df1 = df1.sort_values(by='data')

    # diff()：(当前行-前一行)，如果当前行是第一行则相减后为NaN
    df2 = df1['data'].diff()
    # 把原DataFrame中对应列的第一行值赋值给diff后的DataFrame
    # loc：按照行标签获取行数据
    # df2.loc[0] = df1['data'][0]

    # 使用loc根据行标签获取数据，由于行标签的值会变化，程序报错
    # 解决：把数据类型转换为列表，然后再按照下标获取对应的值
    df2_list = list(df2)
    df2_list[0] = list(df1['data'])[0]

    dic = {'name': list(df1['quarter']), 'value': df2_list}

    return dic


if __name__ == '__main__':
    analyze(2014)

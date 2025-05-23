import requests
import time
import logging
import pandas as pd

'''
获取近十年林业总产值数据
'''

# 关闭告警日志
logging.captureWarnings(True)


def getData():
    # 请求地址
    url = "https://data.stats.gov.cn/search.htm"
    # range(start,end):取值区间：[start,end)，不包含end

    dataList = []

    for year in range(2014, 2024):
        # 休眠时间,单位：秒，在一定程度上避免被网站判定为爬虫机器人，IP被封掉
        time.sleep(3)

        # 请求参数
        param = {
            "s": str(year) +"林业总产值",
            "m": "searchdata",
            "db": "",
            "p": 0
        }
        # verify:关闭验证，requests会自动绕过一部分的验证要求
        # get()：表示使用GET请求方式
        result = requests.get(url=url, params=param, verify=False)
        # print(result.json())
        res = result.json()

        # 值：13.83
        data = res['result'][0]['data']

        # 把年份和data分装成一个元组
        t = (year, data)

        dataList.append(t)

    print(dataList)
    return dataList


def saveData():
    # 获取数据：getData()
    dataList = getData()

    # 把数据转换为pandas的DataFrame
    # columns：指定列名
    df = pd.DataFrame(dataList, columns=['year', 'data'])

    # 保存到csv文件
    # to_csv():把数据保存到csv文件
    # 参数：
    # path:存储文件的路径
    # index=False：在存储数据时忽略行标签
    df.to_csv('forestCount.csv', index=False)


if __name__ == '__main__':
    saveData()

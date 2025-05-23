import requests
import pandas as pd
import time


def getData():
    url = "https://data.stats.gov.cn/search.htm"

    dataList = []
    for year in range(2014, 2024):
        time.sleep(3)

        param = {
            "s": str(year) + "年人均收入",
            "m": "searchdata",
            "db": "",
            "p": 0
        }

        result = requests.get(url, param, verify=False)

        res = result.json()

        print(res)

        t4 = (year, res['result'][3]['sj'], res['result'][3]['data'])
        t3 = (year, res['result'][4]['sj'], res['result'][4]['data'])
        t2 = (year, res['result'][5]['sj'], res['result'][5]['data'])
        t1 = (year, res['result'][6]['sj'], res['result'][6]['data'])

        dataList.append(t1)
        dataList.append(t2)
        dataList.append(t3)
        dataList.append(t4)

    return dataList


def saveData():
    dataList = getData()

    df = pd.DataFrame(dataList, columns=['year', 'quarter', 'data'])
    df.to_csv('salary.csv', index=False)


if __name__ == '__main__':
    saveData()

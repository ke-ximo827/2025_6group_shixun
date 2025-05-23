import requests
import time
import pandas as pd

url = "https://data.stats.gov.cn/easyquery.htm"


def getProvince():
    ts = int(time.time() * 1000)

    param = {
        "m": "getOtherWds",
        "dbcode": "fsnd",
        "rowcode": "zb",
        "colcode": "sj",
        "wds": '[]',
        "k1": ts
    }

    result = requests.get(url, param, verify=False)
    res = result.json()
    print(res)

    nodes = res['returndata'][0]['nodes']

    dataList = []

    for node in nodes:
        code = node['code']
        name = node['name']

        t = (code, name)
        dataList.append(t)

    print(dataList)
    return dataList


def saveProvince():
    dataList = getProvince()

    df = pd.DataFrame(dataList, columns=['code', 'name'])

    df.to_csv('province.csv', index=False)


def getData():
    provinceList = getProvince()

    ts = int(time.time() * 1000)

    dataList = []

    for province in provinceList:
        pCode = province[0]
        pName = province[1]

        for year in (2020, 2023):
            time.sleep(2)

            param = {
                "m": "QueryData",
                "dbcode": "fsnd",
                "rowcode": "zb",
                "colcode": "sj",
                "wds": f'[{{"wdcode":"reg","valuecode":"{pCode}"}}]',
                "dfwds": f'[{{"wdcode":"zb","valuecode":"A0D0504"}},{{"wdcode":"sj","valuecode":"{year}"}}]',
                "k1": ts,
                "h": 1
            }

            result = requests.get(url, param, verify=False)
            res = result.json()

            print(res)

            data = res['returndata']['datanodes'][0]['data']['strdata']

            t = (pName, year, data)

            dataList.append(t)

    return dataList


def saveData():
    dataList = getData()

    df = pd.DataFrame(dataList, columns=['pName', 'year', 'data'])
    df.to_csv('map.csv', index=False)


if __name__ == '__main__':
    saveData()

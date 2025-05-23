import requests
import time
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def getData():
    url = "https://data.stats.gov.cn/search.htm"
    dataList = []

    # 配置重试机制
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    for year in range(2015, 2024):
        time.sleep(5)  # 增加间隔降低封禁风险

        # 优化搜索关键词格式
        param = {
            "s": f"{year}年季度林业总产值",
            "m": "searchdata",
            "db": "",
            "p": 0
        }

        try:
            # 添加请求头模拟浏览器
            response = session.get(
                url,
                params=param,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                },
                verify=False,
                timeout=30
            )
            response.raise_for_status()

            res = response.json()
            print(f"{year}年响应数据：", res)

            # 动态处理结果（不再假设固定4个季度）
            if 'result' in res and len(res['result']) > 0:
                for item in res['result']:
                    # 验证数据格式
                    if all(key in item for key in ['sj', 'data']):
                        # 提取季度信息（示例：从"2023年2季度"提取"Q2"）
                        quarter = f"{year}年第{item['sj'].split('季度')[0][-1]}季度"
                        dataList.append((year, quarter, item['data']))
                    else:
                        print(f"异常数据格式：{item}")
            else:
                print(f"{year}年无有效数据")

        except Exception as e:
            print(f"{year}年请求失败：{str(e)}")
            continue

    return dataList


def saveData():
    dataList = getData()

    # 数据清洗
    df = pd.DataFrame(dataList, columns=['year', 'quarter', 'value'])

    # 去除重复数据
    df = df.drop_duplicates(subset=['year', 'quarter'])

    # 排序保存
    df.sort_values(['year', 'quarter'], inplace=True)
    df.to_csv('forest.csv', index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    saveData()
import pandas as pd
import os


def analyze(year):
    # 获取当前脚本的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建文件路径
    file_path = os.path.join(current_dir, '..', 'spider', 'forest.csv')

    print("File path:", file_path)
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    # 读取文件
    df = pd.read_csv(file_path)

    # 分组获取指定年份数据
    grouped_df = df.groupby('year')
    df_year = grouped_df.get_group(year)

    # 按产值排序（保持原逻辑）
    df_sorted = df_year.sort_values(by='value')

    # 直接使用原始数据
    return {
        'name': df_sorted['quarter'].tolist(),
        'value': df_sorted['value'].tolist()
    }


if __name__ == '__main__':
    result = analyze(2022)
    if result is not None:
        print("季度数据：")
        print(result)
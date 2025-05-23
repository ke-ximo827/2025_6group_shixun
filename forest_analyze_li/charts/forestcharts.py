from analyzer import ForestAnalyzer as fa
from pyecharts.charts import Pie


def pieChart(year):
    dic = fa.analyze(year)

    pie = Pie()

    # zip():将两个数组中对应位置的元素组合成一个元组
    pie.add("林业产值", [list(z) for z in zip(dic['name'], dic['value'])])

    pie_json = pie.dump_options_with_quotes()
    return pie_json

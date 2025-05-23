from pyecharts.charts import Line, Bar
from analyzer import ForestCountAnalyzer as fca
import pyecharts.options as opts

'''
生成echarts图表
'''


def lineChart():
    # 获取analyzer模块中封装好的数据
    dic = fca.analyze()

    # 创建Line折线图对象，填充数据
    line = Line()
    line.add_xaxis(dic['x'])
    line.add_yaxis(series_name="林业总产值", y_axis=dic['y'])
    # 样式全局配置项
    # 关闭x轴和y轴的分隔线
    line.set_global_opts(xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
                         yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)))

    # 把Line转换为json格式
    line_json = line.dump_options_with_quotes()

    return line_json


# 柱状图
# 和折线图生成逻辑一样
# def barChart():
#     dic = fca.analyze()
#
#     bar = Bar()
#     bar.add_xaxis(dic['x'])
#     bar.add_yaxis(series_name='林业总产值', y_axis=dic['y'])
#
#
#     bar_json = bar.dump_options_with_quotes()
#
#     return bar_json

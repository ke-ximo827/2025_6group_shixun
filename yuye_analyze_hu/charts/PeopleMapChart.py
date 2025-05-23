from analyzer import PeopleMapAnalyzer as pma
from pyecharts.charts import Map
import pyecharts.options as opts


def mapChart():
    dataList = pma.analyze()

    map = Map()

    map.add(series_name="各省人口增长比", data_pair=dataList, maptype="china")

    map.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True, is_piecewise=True, pieces=[
        {'max': 0, 'color': 'gray'},
        {'min': 0, 'max': 3, 'color': 'green'},
        {'min': 3, 'max': 6, 'color': 'blue'},
        {'min': 6, 'max': 9, 'color': 'yellow'},
        {'min': 9, 'color': 'red'}

    ], orient='horizontal', pos_left='center'))

    map_json = map.dump_options_with_quotes()

    return map_json

'''
定义接口，和前端页面交互
'''
from django.http import JsonResponse
from charts import AgricultureCountCharts as acc
import json

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# 和前端交互的接口方法
# 参数不能省略，需要接收前端页面传递的请求参数
# def line(request):
#     # 接收前端发送的请求，通过charts模块获取图表数据
#     data = acc.lineChart()
#
#     data = json.loads(data)
#
#     # 做返回数据的封装，将封装好的数据返回前端
#     dic = {"code": 200, "data": data}
#
#     return JsonResponse(dic)


# 柱状图接口


def bar(request):
    data = acc.barChart()

    data = json.loads(data)

    dic = {"code": 200, "data": data}

    response = JsonResponse(dic)

    response["Access-Control-Allow-Origin"] = "*"  # 允许所有来源
    return response

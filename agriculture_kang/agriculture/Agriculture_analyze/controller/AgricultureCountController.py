from django.http import JsonResponse
from charts import AgricultureCountCharts as pcc
import json


# 和前端交互的接口方法
# 参数不能省略，需要接收前端页面传递的请求参数
def line(request):
    # 接收前端发送的请求，通过charts模块获取图表数据
    data = pcc.lineChart()

    data = json.loads(data)

    # 做返回数据的封装，将封装好的数据返回前端
    dic = {"code": 200, "data": data}
    response = JsonResponse(dic)
    response["Access-Control-Allow-Origin"] = "*"  # 允许所有域名访问
    response["Access-Control-Allow-Methods"] = "GET"  # 允许的HTTP方法
    return response


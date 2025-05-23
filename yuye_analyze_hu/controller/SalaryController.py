from django.http import JsonResponse
from charts import SalaryCharts as sc
import json

'''
前端页面请求时会发送参数year
request会接收该参数进行处理
'''


def pie(request):
    # 获取到前端参数类型默认是str
    year = request.GET.get('year')
    # 需要把year转换为int
    data = sc.pieChart(int(year))

    data = json.loads(data)

    dic = {"code": 200, "data": data}

    return JsonResponse(dic)

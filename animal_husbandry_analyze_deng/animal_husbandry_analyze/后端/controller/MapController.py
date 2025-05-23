from django.http import JsonResponse
import json

from charts import MapChart as mc


def map(request):
    data = mc.mapChart()

    data = json.loads(data)

    dic = {"code": 200, "data": data}

    return JsonResponse(dic)

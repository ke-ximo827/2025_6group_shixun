from django.http import JsonResponse
import json

from charts import PeopleMapChart as pmc


def map(request):
    data = pmc.mapChart()

    data = json.loads(data)

    dic = {"code": 200, "data": data}

    return JsonResponse(dic)

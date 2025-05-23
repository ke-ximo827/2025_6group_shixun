from django.http import JsonResponse
from charts import forestcharts as fc
import json

def pie(request):
    year = request.GET.get('year', 'default_year')  # 使用默认值

    if year is None or year.strip() == '':
        return JsonResponse({"code": 400, "message": "Missing or empty 'year' parameter"}, status=400)
    try:
        year = int(year)
    except ValueError:
        return JsonResponse({"code": 400, "message": "Invalid 'year' parameter, must be an integer"}, status=400)
    data = fc.pieChart(year)
    try:
        data = json.loads(data)
    except json.JSONDecodeError:
        return JsonResponse({"code": 500, "message": "Failed to parse data as JSON"}, status=500)
    dic = {"code": 200, "data": data}
    return JsonResponse(dic)
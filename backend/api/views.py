
import json
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    # Request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    body = request.body   # byte string JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)

    # return JsonResponse({"message": "Hi There, this is your Django Api Rasponce!!"})

import json
from django.http import JsonResponse
from products.models import Product

# Create your views here.
def api_home(request, *args, **kwargs):

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)

    # # return JsonResponse({"message": "Hi There, this is your Django Api Rasponce!!"})
    #     # Request -> HttpRequest -> Django
    # # print(dir(request))
    # # request.body
    # body = request.body   # byte string JSON data
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
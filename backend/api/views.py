
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product

from products.serializers import ProductSerializer

# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id','title','price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)

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
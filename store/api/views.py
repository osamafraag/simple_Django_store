
from rest_framework.response import Response
from rest_framework.decorators import api_view
from store.models import Product
from store.api.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response({"messsage": 'object add received', "student":product.data}, status=201)
        return Response(product.errors, status=400)

    elif request.method=='GET':
        products = Product.products() 
        serlized_products = ProductSerializer(products, many=True)
        return Response({"message": "students data receieved", 'students': serlized_products.data})



@api_view(['GET', 'DELETE', 'PUT'])
def product_data(request, id):
    product = Product.get(id)
    if request.method=='GET':
        serlized_product = ProductSerializer(product)
        return Response({'data':serlized_product.data}, status=200)

    elif request.method=='DELETE':
        product.delete()
        return Response({"message":"object deleted"}, status= 204)

    elif request.method=="PUT":
        serlized_product = ProductSerializer(instance=product,data=request.data)
        if serlized_product.is_valid():
            serlized_product.save()
            return Response({"messsage": 'object add received', "product": serlized_product.data}, status=201)
        return Response(serlized_product.errors, status=400)
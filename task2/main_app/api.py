from rest_framework.generics import ListAPIView

from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductApi(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryApi(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

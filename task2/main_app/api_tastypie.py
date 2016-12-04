from tastypie.resources import ModelResource
from tastypie.constants import ALL

from .models import Product


class ProductrResource(ModelResource):

    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        filtering = {'name': ALL}

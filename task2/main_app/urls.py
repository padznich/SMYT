from django.conf.urls import url

from .api import ProductApi, CategoryApi

urlpatterns = [

    #REST
    url(r'^products$', ProductApi.as_view()),
    url(r'^categories$', CategoryApi.as_view())
]
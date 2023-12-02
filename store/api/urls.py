
from django.urls import path
from store.api.views import index, product_data

urlpatterns = [
    path('', index, name='api.index'),
    path('<int:id>',product_data, name='product_data')
]
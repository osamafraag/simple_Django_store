

from django.urls import path, include
from store.views import (contactUs, aboutUs, details,index, delete, createViaForm, editViaForm,CreateProduct,EditProduct)

urlpatterns = [
    path('index/', index,name="index"),
    path('api/', include('store.api.urls')),
    path('contactUs',contactUs, name='contactUs'),
    path('aboutUs', aboutUs , name='aboutUs'),
    path("<int:id>", details,name="product.details"),
    path('delete/<int:id>', delete,name="product.delete"),
    path('edit/<int:id>', editViaForm,name="product.edit"),
    path('create/', createViaForm,name="product.create"),
    # path('edit/<int:id>', EditProduct.as_view(),name="product.edit"),
    # path('create/', CreateProduct.as_view(),name="product.create")

] 

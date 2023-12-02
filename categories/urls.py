
from django.contrib.auth.decorators import login_required
from django.urls import path
from categories.views import (index, details, delete, edit, create,
            CategoryDelete,CategoryCreate,CategoryUpdate,CategoryDetails,CategoriesList)

urlpatterns = [

    # path('index', index, name='category.index'),
    # path('details/<int:id>', details , name='category.details'),
    # path('delete/<int:id>', delete, name='category.delete'),
    # path('forms/edit/<int:id>', edit, name='category.edit'),
    # path('forms/create', create, name='category.create'),
    path('index', CategoriesList.as_view(), name='category.index'),
    path('details/<int:pk>', CategoryDetails.as_view() , name='category.details'),
    path('delete/<int:pk>', login_required(CategoryDelete.as_view()), name='category.delete'),
    path('forms/edit/<int:pk>', login_required(CategoryUpdate.as_view()), name='category.edit'),
    path('forms/create', login_required(CategoryCreate.as_view()), name='category.create'),
] 

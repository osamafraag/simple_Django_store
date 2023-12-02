from django.urls import  path, include
from django.contrib.auth.decorators import login_required
from accounts.views import profile, CreateCustomUser, userLogin, userLogout,UserUpdate,UserDelete
urlpatterns = [

    path('/', include('django.contrib.auth.urls')),
    path('profile/' , profile, name='account.profile'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('register/',CreateCustomUser.as_view(), name='account.create'),
    path('delete/<int:pk>', login_required(UserDelete.as_view()), name='account.delete'),
    path('edit/<int:pk>', login_required(UserUpdate.as_view()), name='account.edit'),

]
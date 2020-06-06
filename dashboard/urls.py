from django.contrib import admin
from django.urls import include,path 
from . import views 

from rest_framework import routers
from .rest import api 




router = routers.DefaultRouter()
router.register(r'/sale', api.SaleViewSet)
router.register(r'/stockitem', api.StockItemViewSet)
router.register(r'/user', api.UserViewSet)

urlpatterns = [

    path('', views.indexpage),
    # path('login', views.login),
    
    # path('api',  include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'),)
    #     path('user', logged.HomeView.as_view() ),
	#     path('proregister', pages.prosignuppage ),
	#     path('userregister', pages.signuppage ),
	path('api',  include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'),)


]
from django.contrib import admin
from django.urls import include,path 
from . import views 


urlpatterns = [

    path('', views.indexpage),
    # path('login', views.login),
    
    # path('api',  include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'),)
    #     path('user', logged.HomeView.as_view() ),
	#     path('proregister', pages.prosignuppage ),
	#     path('userregister', pages.signuppage ),

]
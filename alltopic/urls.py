
from django.contrib import admin
from django.urls import path
from myapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('details/<str:c_code>/', views.details, name='details'), 
    
    
]

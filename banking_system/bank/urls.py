from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:id>/', views.customer_detail, name='customer_detail'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('transfer/<int:customer_id>/', views.transfer, name='transfer'),
]

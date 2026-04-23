from django.urls import path
from . import views

# localhost:8000/app1/ --> app1 page
# localhost:8000/app1/order/ --> order page
urlpatterns = [
    path('', views.app1, name='app1'), # App1 page
    # path('order/', views.order, name='order')
]
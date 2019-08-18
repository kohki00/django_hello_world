from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('hello_world/', views.hello_view, name='hello')
]

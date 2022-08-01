from django.urls import path
from .views import infotodb, index

urlpatterns = [
    path('dbrefresh/', infotodb, name='dbrefresh'),
    path('index/', index, name='index'),
]

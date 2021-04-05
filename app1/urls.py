from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    path("",views.index,name="index"),
    path("sam1/",views.sam1,name="sam1")
]
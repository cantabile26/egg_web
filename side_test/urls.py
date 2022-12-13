from django.urls import path
from side_test import views

app_name = "side_test"

urlpatterns = [
    path('egg/', views.egg_info_view, name="egg_info"),

]


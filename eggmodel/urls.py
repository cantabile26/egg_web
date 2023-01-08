from django.urls import path
from eggmodel import views

app_name = "eggmodel"

urlpatterns = [
  path('', views.view_egg_model, name="eggModelView")
]

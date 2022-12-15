from django.urls import path
from egg_info import views

app_name = "egg_info"

urlpatterns = [
    path('egg_info/', views.egg_info_view, name="egg_info"),
    path('egg_data_upload/', views.egg_data_upload_view, name="egg_data_upload"),
]


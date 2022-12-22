from django.urls import path
from egg_info import views

app_name = "egg_info"

urlpatterns = [
    path('egg_info/', views.egg_info_view, name="egg_info"),
    # path('egg_info/', views.egg_info_modal, name="egg_info_modal"),

    path('farm_management/', views.farm_management_view, name="farm_management"),

]
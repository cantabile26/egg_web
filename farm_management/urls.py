from django.urls import path
from farm_management import views

app_name = "farm_management"

urlpatterns = [
    path('farm_management/', views.farm_management_view, name="farm_management"),
    path('farm_register/', views.farm_register_view, name="farm_register"),

]
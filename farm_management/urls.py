from django.urls import path
from farm_management import views

app_name = "farm_management"

urlpatterns = [
    # path('farm_register/', views.farm_register_view, name="farm_register"),
    path('farm_management/', views.farm_management_view, name="farm_management"),

    # farm 등록
    path('farm_list/', views.farm_list_up, name="farmListPage"),
    path('farm_insert/', views.farm_insert_view, name="farmInsertPage"),

    # barn 등록
    path('barn_list/', views.barn_list_up, name="barnListPage"),
    path('barn_insert/', views.barn_insert_view, name="barnInsertPage"),

]
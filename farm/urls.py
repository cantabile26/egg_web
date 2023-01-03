from django.urls import path
from farm import views

app_name = "farm"

urlpatterns = [
    # path('farm_register/', views.farm_register_view, name="farm_register"),
    path('', views.farm_view, name="farmViewPage"),

    # # farm 등록
    # path('farm_list/', views.farm_list_up, name="farmListPage"),
    # path('farm_insert/', views.farm_insert_view, name="farmInsertPage"),

    # # barn 등록
    # path('barn_list/', views.barn_list_up, name="barnListPage"),
    # path('barn_insert/', views.barn_insert_view, name="barnInsertPage"),
    # # barn 수정
    # path('barn_update/', views.barn_update, name="barnUpdatePage"),
]
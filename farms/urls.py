from django.urls import path
from farms import views

app_name = "farms"

urlpatterns = [
    path('', views.farm_view, name="farmViewPage"),
    path('farm_list/', views.farm_list_view, name="farmListPage"),
    # farm 등록
    path('farm_insert/', views.farm_insert_view, name="farmInsertPage"),
    path('farm_update/<str:farm_code>', views.farm_update_view, name="farmUpdatePage"),

    # # barn 등록
    # path('barn_list/', views.barn_list_up, name="barnListPage"),
    # path('barn_insert/', views.barn_insert_view, name="barnInsertPage"),
    # # barn 수정
    # path('barn_update/', views.barn_update, name="barnUpdatePage"),
]
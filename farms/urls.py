from django.urls import path
from farms import views

app_name = "farms"

urlpatterns = [
    path('', views.farm_view, name="farmViewPage"),
    # farm 정보
    path('farm_list/', views.farm_list_view, name="farmListPage"),
    # farm 등록
    path('farm_insert/', views.farm_insert_view, name="farmInsertPage"),
    # farm 수정
    path('farm_update/<str:farm_code>', views.farm_update_view, name="farmUpdatePage"),

    # # barn 리스트
    path('barn_list/', views.barn_list, name="barnListPage"),
    # barn 등록
    path('barn_insert/', views.barn_insert_view, name="barnInsertPage"),
    # barn 수정
    path('barn_update/<int:barn_code>', views.barn_update_view, name="barnUpdatePage"),
    # barn 삭제
    path('barn_delete/<int:barn_code>', views.barn_delete, name="barnDelete"),
]
from django.urls import path
from dev import views

app_name = "dev"

urlpatterns = [
    path('code/', views.code_view, name="codeListPage"),
    # 상위코드
    path('code_up_list/', views.code_up_list, name="codeUpList"),
    path('code_up_insert/', views.code_up_add, name="codeUpInsertPage"),
    
    path('add_movie/', views.add_movie, name="add_movie"),
]



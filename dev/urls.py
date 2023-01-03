from django.urls import path
from dev import views

app_name = "dev"

urlpatterns = [
    path('code/', views.code_view, name="codeListPage"),
    # 상위코드
    path('code_up_list/', views.view_code_up_list, name="codeUpList"),
    path('code_up_insert/', views.code_up_add, name="codeUpInsertPage"),
    path('code_up_update/<int:code_up_code>', views.code_up_update, name="codeUpdatePage"),
    # 하위코드
    path(r'code_down_list/<int:code_up>', views.view_code_down_list, name="codeDownList"),
    
]



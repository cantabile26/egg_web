from django.urls import path
from dev import views

app_name = "dev"

urlpatterns = [
    path('code/', views.code_view, name="codeListPage"),
    # 상위코드
    path('code_up_list/', views.view_code_up_list, name="codeUpList"),
    path('code_up_insert/', views.code_up_add, name="codeUpInsertPage"),
    path('code_up_update/<int:code_up_code>', views.code_up_update, name="codeUpdatePage"),
    path('code_up_delete/<int:code_up_code>', views.code_up_delete, name="codeUpDelete"),
    # 하위코드
    path(r'code_down_list/<int:code_up>', views.view_code_down_list, name="codeDownList"),
    path('code_down_insert/<int:code_up_code>', views.code_down_add, name="codeDownInsertPage"),
    path('code_down_update/<int:code_up_code>/<int:code_down_code>', views.code_down_update, name="codeDownUpdatePage"),
    path('code_down_delete/<int:code_up_code>/<int:code_down_code>', views.code_down_delete, name="codeDownDelete"),
    
]



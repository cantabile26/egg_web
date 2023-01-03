from django.urls import path
from dev2 import views

app_name = "dev2"

urlpatterns = [
    path('usermanage/', views.user_manage, name="usermanagePage"),
    path('uuser_up_list/', views.view_uuser_list, name="uuserUpList"),

    path('aaa/<int:id>', views.aaa, name="aaaPage"),
]

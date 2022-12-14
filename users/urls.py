from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('', views.login_view, name="loginPage"),
    path('signup/', views.user_register, name="signUpPage"),
    path('logout/', views.logoutAction, name="logout"),
    # 관리자 메뉴 
    path('list/', views.users_list_view, name="userlistViewPage"),
    path('list_data/', views.users_list, name="userlist"),
    path('user_update/<int:user_code>', views.user_update_view, name="userUpdateViewPage")
]


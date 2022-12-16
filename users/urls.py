from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('singin/', views.sign_in_table, name="sign_in_tablePage"),
    path('singup2/', views.sign_up_table, name="sign_up_tablePage"),
    # path('users/'. views.test, name="testPage"),
    path('', views.login_view, name="loginPage"),
    path('signup/', views.user_register, name="signUpPage"),
    path('logout/', views.logoutAction, name="logout"),
    # 관리자 메뉴 
    path('list/', views.users_list_view, name="userlistViewPage")
]

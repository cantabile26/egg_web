from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('singin/', views.sign_in_table, name="sign_in_tablePage"),
    path('singup/', views.sign_up_table, name="sign_up_tablePage"),
    # path('users/'. views.test, name="testPage"),
]

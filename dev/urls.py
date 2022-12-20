from django.urls import path
from dev import views

app_name = "dev"

urlpatterns = [
    path('code/', views.code_view, name="codeListPage"),
    path('code_up_insert/', views.code_up_add, name="codeUpInsertPage"),
    path('add_movie/', views.add_movie, name="add_movie"),
]



from django.urls import path
from eggtemp import views

app_name = "eggtemp"

urlpatterns = [
    path('buttons/', views.buttonView, name="buttonViewPage"),
    path('notification/', views.notificationView, name="notificationViewPage"),
    path('forms/', views.formsView, name="formsViewPage"),
    path('modals/', views.modalsView, name="modalsViewPage"),
    path('typography/', views.typographyView, name="typographyViewPage"),
    path('gridtest/', views.gridtestView, name="gridtestViewPage"),
]


from django.urls import path
from eggpagetemp import views

app_name = "eggpagetemp"

urlpatterns = [
    path('sign-in/', views.signInView, name="signInViewPage"),
    path('sign-out/', views.signOutView, name="signOutViewPage"),
    path('forgot-pass/', views.forgotPassView, name="forgotPassViewPage"),
    path('reset-pass/', views.resetPassView, name="resetPassViewPage"),
    path('page-lock/', views.pageLockView, name="pageLockViewPage"),
    path('page-403/', views.page403View, name="page403ViewPage"),
    path('page-404/', views.page404View, name="page404ViewPage"),
    path('page-500/', views.page500View, name="page500ViewPage"),
]


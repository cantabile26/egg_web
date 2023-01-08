from django.urls import path
from eggprice import views

app_name = "eggprice"

urlpatterns = [
    path('', views.price_view, name="priceViewPage"),
    path('egg_price_list/<str:start_date>/<str:end_date>', views.price_data_list, name="priceViewList"),
]
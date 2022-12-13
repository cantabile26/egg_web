from django.urls import path
from eggtabletemp import views

app_name = "eggtabletemp"

urlpatterns = [
  path('bootstrap-tables/', views.bootstrapTables, name="bootstrapTablesPage"),
]


from django.urls import path
from eggtabletemp import views

app_name = "eggtabletemp"

urlpatterns = [
  path('bootstrap-tables/', views.bootstrapTables, name="bootstrapTablesPage"),
  path('eggdetect-tables/', views.eggdetectTables, name="eggdetectTablesPage"),
  path('eggmanage-tables/', views.eggmanageTables, name="eggmanageTablesPage"),
  path('eggmanage-input-tables/', views.eggmanageinputTables, name="eggmanageinputTablesPage"),
  path('createform/', views.createform, name='createform'),
]


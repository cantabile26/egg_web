from django.urls import path
from eggmanage import views

app_name = "eggmanage"

urlpatterns = [
        path('eggmanage-tables/', views.eggmanageTables, name="eggmanageTablesPage"),
        path('eggmanage-input-tables/', views.eggmanageinputTables, name="eggmanageinputTablesPage"),
        path('createform/', views.createform, name='createform'),

        #path('update_account/<str:회계코드>', views.update_account, name="updateaccountPage"),
]



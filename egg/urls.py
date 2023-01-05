from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import urls as main
from users import urls as users
from dev import urls as dev
from farms import urls as farms
from eggmodel import urls as eggmodel
from eggtemp import urls as eggtemp
from eggpagetemp import urls as eggpagetemp
from eggtabletemp import urls as eggtabletemp


urlpatterns = [
    path('admin/', admin.site.urls),
    #main
    path('', include(main)),
    #users - login, logout
    path('users/', include(users)),
    #dev - 관리자 페이지
    path('dev/', include(dev)),
    #farm
    path('farm/', include(farms)),
    #eggmodel
    path('eggmodel', include(eggmodel)),
    #template 
    path('eggtemp/', include(eggtemp)),
    path('eggpagetemp/', include(eggpagetemp)),
    path('eggtabletemp/', include(eggtabletemp)),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)


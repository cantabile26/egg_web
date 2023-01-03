from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import urls as main
from users import urls as users
from dev import urls as dev
from dev2 import urls as dev2
from eggtemp import urls as eggtemp
from eggpagetemp import urls as eggpagetemp
from eggtabletemp import urls as eggtabletemp
from eggmanage import urls as eggmanage

urlpatterns = [
    path('admin/', admin.site.urls),
    #main
    path('', include(main)),
    #users - login, logout
    path('users/', include(users)),
    #dev - 관리자 페이지
    path('dev/', include(dev)),
    path('dev2/', include(dev2)),
    #template 
    path('eggtemp/', include(eggtemp)),
    path('eggpagetemp/', include(eggpagetemp)),
    path('eggtabletemp/', include(eggtabletemp)),
    path('eggmanage/', include(eggmanage)),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)


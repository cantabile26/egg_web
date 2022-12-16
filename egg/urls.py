from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import urls as main
from users import urls as users
from eggtemp import urls as eggtemp
from egg_info import urls as egg_info
from eggpagetemp import urls as eggpagetemp
from eggtabletemp import urls as eggtabletemp

urlpatterns = [
    path('admin/', admin.site.urls),
    #main
    path('', include(main)),
    #users - login, logout
    path('users/', include(users)),
    #template 
    path('eggtemp/', include(eggtemp)),
    path('egg_info/', include(egg_info)),
    path('eggpagetemp/', include(eggpagetemp)),
    path('eggtabletemp/', include(eggtabletemp)),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)


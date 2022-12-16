from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import urls as main
from eggtemp import urls as eggtemp
from eggpagetemp import urls as eggpagetemp
from eggtabletemp import urls as eggtabletemp
from users import urls as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main)),
    path('users/', include(users)),
    path('eggtemp/', include(eggtemp)),
    path('eggpagetemp/', include(eggpagetemp)),
    path('eggtabletemp/', include(eggtabletemp)),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)


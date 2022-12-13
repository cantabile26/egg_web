from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import urls as main
from eggtemp import urls as eggtemp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main)),
    path('eggtemp/', include(eggtemp)),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)

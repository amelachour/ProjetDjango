from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path("/", include("apps.authentication.urls")),
    path("", include("apps.home.urls")),
    path("cours/", include("apps.cours.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls"))  ,           # UI Kits Html files
    path("", include("apps.cours.urls"))  , 
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> c4f4019b0ff2ad6983f6bd24f6b5f3e4a8431bde

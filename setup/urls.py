from django.contrib import admin
from django.urls import path, include
from lista.views import ListaViewSet
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="lista",
      default_version='v1',
      description="Lista de desejos",
      terms_of_service="#",
      contact=openapi.Contact(email="rhama.krisner@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('produto', ListaViewSet, basename='Produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

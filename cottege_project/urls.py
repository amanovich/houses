from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter




schema_view = get_schema_view(
   openapi.Info(
      title="Property API",
      default_version='v1',
      description="Документация по недвижимости",
   ),
   public=True,
   permission_classes=(AllowAny,),
)


urlpatterns = [


    path('admin/', admin.site.urls),
    path('api/', include('houses.api_urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # <-- путь
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


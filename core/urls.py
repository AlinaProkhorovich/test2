from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core.views import home
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from cohorts import views
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'cohorts', views.CohortViewSet, basename='cohort')
router.register(r'memberships', views.CohortMembershipViewSet, basename='membership')

schema_view = get_schema_view(
   openapi.Info(
      title="Cohort Test Platform API",
      default_version='v1',
      description="API for managing cohorts and tests",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@cohortplatform.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
from django.urls import path
from .import views 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="platfr ",
      default_version='v1',
      description="API documentation for Register and Login",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = {
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),

}



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
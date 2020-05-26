from django.urls import path
from . import views
from . import dash_apps
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='catalog-home'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
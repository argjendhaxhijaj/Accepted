from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='accepted-index'),
    path('success-stories', views.successs, name='accepted-successs'),
    path('places', views.places, name='accepted-places'),
    path('events', views.events, name='accepted-events'),
    path('submit', views.submit, name='accepted-submit'),
    path('about', views.about, name='accepted-about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
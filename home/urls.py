from django.urls import path
from .views import home
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home, name='home'),
    path("doctor/",views.get_doctors_by_department, name="get_doctors_by_department"),
    path('doctor/create/', views.create_doctor, name='create_doctor'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
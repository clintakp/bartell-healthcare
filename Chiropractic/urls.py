from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns  = {
    path('', views.index, name="index"),
    path('', views.home, name="home"),
    path('about_us', views.about_us, name="about_us"),
    path('what_is_chiropractic', views.what_is_chiropractic, name="what_is_chiropractic"),
    path('office_hours', views.office_hours, name="office_hours"),
    path('services', views.services, name="services"),
    path('contact_us', views.contact_us, name="contact_us"),
}
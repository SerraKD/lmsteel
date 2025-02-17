"""
URL configuration for lmsteel project.

"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from steelbusiness import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-language/', views.set_language, name='set_language'),
    path('', views.home, name='home'),  # Root URL pattern
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('staircase/', views.staircase, name='staircase'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)
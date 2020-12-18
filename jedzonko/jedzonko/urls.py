"""jedzonko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers, serializers
from jedzenie.views import RestauracjaView,TypRestauracjiView,WlascicielView,AdresView,KlientlView,PozycjaView,MenuView,OpiniaORestauracjiView,ZamowienieView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'restauracja', RestauracjaView)
router.register(r'typrestauracji', TypRestauracjiView)
router.register(r'wlasciciel', WlascicielView)
router.register(r'adres', AdresView)
router.register(r'klient', KlientlView)
router.register(r'pozycja', PozycjaView)
router.register(r'menu', MenuView)
router.register(r'opiniaorestauracji',OpiniaORestauracjiView)
router.register(r'zamowienie', ZamowienieView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

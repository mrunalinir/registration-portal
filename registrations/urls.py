"""registrations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpa,mtterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
import event.views
import contingent.views


urlpatterns = [
    path('', views.index, name="home"),
    path('event/', event.views.event, name='event'),
    path('contingent/', contingent.views.contingent, name='contingent'),
    path('done/', views.done, name="fin"),
    path('registrations/', event.views.display, name='eventdone'),
	path('admin/', admin.site.urls),
]

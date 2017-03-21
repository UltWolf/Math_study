"""Math URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Math import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Tasks.views import Tasks
import registration.backends.simple.urls
import index.urls
import Authorization.urls
from Theory.views import List_Theory
from Tasks.views import Tasks,Task_all
from Authorization.views import profile
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'profile/(?P<username>[\w\-]+)/$',profile),
    url(r'^auth/',include(Authorization.urls)),
    url(r'^theory/',List_Theory),
    url(r'task/',Task_all),
    url(r'^tasks/(?P<Tasks_name_slug>[\w\-]+)/$', Tasks, name='category'),

    url(r'',include(index.urls)),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

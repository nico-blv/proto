"""prototipo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from prototipo import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from core import views as core_views
from dashboard import views as dash_views

#ADMIN

admin.site.site_header = 'PROFATTENING'
admin.site.site_title = 'Admin Profattening'
admin.site.index_title = 'Panel de administración'
admin.site.site_url = '/dashboard'

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls),
    path('dashboard/', dash_views.home, name="dashboard"),
    path('grafico/', dash_views.grafico, name="grafico"),
    path('listado/', dash_views.list, name="listado"),
    path('lote/', dash_views.lote, name="lote"),
    path('login/', LoginView.as_view(template_name='dashboard/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
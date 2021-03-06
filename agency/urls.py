"""agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from dash import views as dash_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns as statics
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # system configs:
	path('admin/', admin.site.urls),

	# landing page:
    path('', dash_views.index),
	
	# authentication:
	path('giris/', auth_views.LoginView.as_view(template_name='templates/login.html')),
	
	# registration
	path('yenihesap/', dash_views.register),

	# catalogue of actors
	path('katalog/ekle', dash_views.add_new_actor),
	path('katalog/', dash_views.catalogue),

	re_path(r'^katalog/(?P<actorid>\d+)$', dash_views.portfolio_public),
	re_path(r'^katalog/(?P<actorid>\d+)/full$', dash_views.portfolio_private),

]

urlpatterns += statics()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

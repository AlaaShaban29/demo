"""ADHOC URL Configuration

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
from django.contrib import admin
from django.urls import path, include ,re_path as url

from django.conf import settings
from django.conf.urls.static import static

# from rest_framework.authtoken import views
# from adhoc_mobile.admin import custom_site 


urlpatterns = [
        path("admin/", admin.site.urls),

#    path("projectAdmin/", custom_site.urls),

        path('summernote/', include('django_summernote.urls')),
url(r'^advanced_filters/', include('advanced_filters.urls')),
    # path('api-token-auth/', views.obtain_auth_token),

            path('_nested_admin/', include('nested_admin.urls')), # Here

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


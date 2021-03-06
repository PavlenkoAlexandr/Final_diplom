"""backend URL Configuration

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
from django.urls import path
from orders import urls as orders_urls
from products import urls as products_urls
from shops import urls as shops_urls
from users import urls as users_urls
from authorization import urls as auth_url
from partner import urls as partner_url

urlpatterns = [
    path('admin/', admin.site.urls),
] + orders_urls.urlpatterns + products_urls.urlpatterns + shops_urls.urlpatterns + users_urls.urlpatterns + \
              auth_url.urlpatterns + partner_url.urlpatterns

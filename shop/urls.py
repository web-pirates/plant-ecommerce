"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from page import views as p_views

urlpatterns = [
    path('', p_views.index, name='index'),
    path('category/', p_views.scategory, name='category'),
    path('detail/', p_views.pdetail, name='detail'),
    path('checkout/', p_views.pcheckout, name='checkout'),
    path('cart/', p_views.shoppingcart, name='cart'),
	path('confirmation/', p_views.confirmation, name='confirmation'),
	path('dbform/', p_views.dbform, name='dbform'),
    path('admin/', admin.site.urls),
]

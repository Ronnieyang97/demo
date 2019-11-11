"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from demo_app.views import test, index
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    # path('test/<a>/<b>/', test),
    path('newtest/<a>/<b>/', test, name='test')  # name的作用是将test函数能与html文件对应起来，当地址变化时仍然能准确调用函数


]

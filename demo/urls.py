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
from django.urls import path, re_path
from demo_app.views import *
import re
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('books/', BookView.as_view(), name='get'),  # 使用.as_view()才能正确连接到get函数
    path('title/<str:title>/', BookViewTitle.as_view(), name='get_title'),
    path('author/<str:author>/', BookViewAuthor.as_view(), name='get_author'),
    path('type/<str:booktype>/', BookViewType.as_view(), name='get_type'),
    path('one/<str:dbid>', BookViewOne.as_view(), name='get_id'),
    path('create/', BookCreate.as_view(), name='create'),
]

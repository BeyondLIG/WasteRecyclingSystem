"""WasteRecyclingSystem URL Configuration

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
from django.urls import path, include, re_path

import xadmin
from django.views.static import serve

from WasteRecyclingSystem.settings import MEDIA_ROOT
from apps.user.views import IndexView, RegisterView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("xadmin/", xadmin.site.urls),
    path("captcha/", include('captcha.urls')),

    # media
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),

    # 首页
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view(), name="index"),

    # user app
    path('user/', include('user.urls', namespace='user')),

    # order app
    path('order/', include('order.urls', namespace='order')),

    # scrap app
    path('scrap/', include('scrap.urls', namespace='scrap')),

]

# 配置全局404变量
handler404 = 'user.views.page_not_found'
# 配置全局500变量
# handler500 = 'user.views.page_error'

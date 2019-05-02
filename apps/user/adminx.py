# -*- coding: utf-8 -*-
# @DATE    : 2019/4/4
# @Author  : licg
# @Email   : licgbeyond@foxmail.com
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

from .models import UserProfile, Banner


class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'gender', 'phone', 'address', 'role']
    search_fields = ['username', 'gender', 'phone', 'address', 'role']
    list_filter = ['role']


# xadmin的全局配置管理器
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# xadmin全局配置参数信息设置
class GlobalSettings(object):
    site_title = '废品回收系统'
    site_footer = 'WHUT'
    menu_style = 'accordion'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Banner, BannerAdmin)


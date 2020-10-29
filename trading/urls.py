
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from accounts import urls as accounts_urls
from main import urls as main_urls
from trader import urls as trader_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include(accounts_urls)),
    path('', include(main_urls)),
    path('trader/', include(trader_urls)),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

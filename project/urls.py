from django.conf.urls import patterns, include, url
from django.contrib import admin
from calc import views

urlpatterns = (
    url(r'^$', views.default),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)\+(\d+)$', views.sum),
    url(r'^(\d+)\-(\d+)$', views.subs),
    url(r'^(\d+)\*(\d+)$', views.mult),
    url(r'^(\d+)\/(\d+)$', views.div),
    url(r'', views.notFound),
)

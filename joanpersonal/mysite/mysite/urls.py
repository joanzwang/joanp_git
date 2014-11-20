from django.conf.urls import patterns, include, url
from mysite import views as v

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^home/$', v.index),
    url(r'^contact/$', v.contact),
    url(r'^admin/', include(admin.site.urls)),
)

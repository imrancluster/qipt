from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from qipt import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qipt.views.home', name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^telephony/', include('telephony.urls', namespace="telephony")),
    url(r'^admin/', include(admin.site.urls)),
)

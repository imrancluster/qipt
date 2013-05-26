from django.conf.urls import patterns, include, url

from telephony import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^sendemail/$', views.sendemail, name='sendemail'),

    # user login logout
    url(r'^user_login/$', views.user_login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    # user management for asterisk account
    url(r'^users/$', views.alluser, name='users'),
    url(r'^user/add/$', views.adduser, name='adduser'),
    url(r'^user/(?P<uid>\d+)/edit/$', views.edituser, name='edituser'),
    url(r'^user/(?P<uid>\d+)/delete/$', views.deleteuser, name='deleteuser'),

    # sip file configuration
    url(r'^applyzone/$', views.applyzone, name='applyzone'),
    url(r'^sip/$', views.sip, name='sip'),


    url(r'^thanks/$', views.thanks, name='thanks'),

    #user guide
    url(r'^doc/$', views.doc, name='doc'),

    #Search
    url(r'^search/$', views.search, name='search')
)

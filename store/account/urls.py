from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = patterns(
    '',
    url(r'^login/$', auth_views.login, name='login',
        kwargs={'template_name': 'account/login.html'}),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'template_name': 'account/logged_out.html'}),
    url(r'^password_change/$', auth_views.password_change, name='password_change',
        kwargs={'template_name': 'account/password_change.html',
                'post_change_redirect': 'done/'}),
    url(r'^password_change/done/$', auth_views.password_change_done,
        name='password_change_done',
        kwargs={'template_name': 'account/password_change_done.html'}),


    url(r'^profile/$', views.profile, name='profile'),

)

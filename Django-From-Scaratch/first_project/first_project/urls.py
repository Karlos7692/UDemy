from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Admin
    url(r'^admin/', include(admin.site.urls)),

    #Login U
    url(r'^accounts/log_in', 'first_project.views.log_in'),
    url(r'^accounts/authenticate', 'first_project.views.authenticate'),
    url(r'^accounts/logged_in', 'first_project.views.logged_in'),
    url(r'^accounts/log_out', 'first_project.views.log_out'),
    url(r'^accounts/invalid_log_in', 'first_project.views.invalid_log_in'),


    #Articles URLS

    url(r'^articles/', include('article.urls'))



)

from django.conf.urls import patterns, include, url
from views import HelloTemplate
urlpatterns = patterns('',

    #Hello World!
    url(r'^hello/$', 'article.views.hello'),
    url(r'^hello_template/$', 'article.views.hello_template'),
    url(r'^hello_template_simple', 'article.views.hello_template_simple'),
    url(r'hello_class_view', HelloTemplate.as_view()),

    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.set_language')

)
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView
from models import Article


#Quick tutorial on Views
def hello(request):
    name = 'Karl'
    html = "<html><body>Hi %s. This seemed to have worked!</body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = 'Karl'
    t = get_template('hello_template.html')
    html = t.render(Context({'name' : name}))
    return HttpResponse(html)


def hello_template_simple(request):
    name = "Karl"
    return render_to_response('hello_template.html', {'name' : name})


class HelloTemplate(TemplateView):

    template_name = 'hello_class_template.html'


    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Karl'
        return context


#Article Views
def articles(request):

    cookie_language = 'en-aus'
    session_language = 'en-aus'

    if 'lang' in request.COOKIES:
        cookie_language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    articles = Article.objects.all()
    return render_to_response('articles.html',
                              {'articles' : articles,
                              'cookie_language': cookie_language,
                              'session_language': session_language})

def article(request, article_id=1):
    article = Article.objects.get(id=article_id)
    return render_to_response('article.html',
        {'article' : article})

#Cookie and Session Demonstration
def set_language(request, language='en-aus'):
    response = HttpResponse("Setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response
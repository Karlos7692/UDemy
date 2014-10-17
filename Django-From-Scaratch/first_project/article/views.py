from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView
from models import Article
from models import Comment
from forms import ArticleForm
from forms import CommentForm
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.utils import timezone


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

    values = {}
    values.update(csrf(request))
    values['articles'] = articles
    values['cookie_language'] = cookie_language
    values['session_language'] = session_language

    return render_to_response('articles.html', values)

def article(request, article_id=1):
    article = Article.objects.get(id=article_id)
    return render_to_response('article.html',
        {'article' : article})


def create_article(request):
    values = {}
    values.update(csrf(request))
    values['form'] = ArticleForm()
    page = render_to_response("create_article.html", values)
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            page = HttpResponseRedirect('/articles/all')

    return page


def like_article(request, article_id=0):
    if article_id:
        article = Article.objects.get(id=article_id)
        article.likes += 1
        article.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)


def add_comment(request, article_id):

    print article_id
    a = Article.objects.get(id=article_id)

    values = {}
    values.update(csrf(request))

    values['form'] = CommentForm()
    values['article'] = a

    page = render_to_response("add_comment.html", values)
    print "Checking whether a form was submitted"
    print request.method
    if request.method == 'POST':
        print "Form submitted"
        f = CommentForm(request.POST)
        if f.is_valid():
            print "Form is valid"
            c = f.save(commit=False)

            c.pub_date = timezone.now()
            c.article = a
            c.save()
            page = HttpResponseRedirect('/articles/get/%s' % article_id)

    return page

#AJAX Methods
def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    print "|",search_text,"|"
    articles = Article.objects.filter(title__contains=search_text)
    print articles
    return render_to_response('ajax_search.html', {'articles' : articles})


#Cookie and Session Demonstration
def set_language(request, language='en-aus'):
    response = HttpResponse("Setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response
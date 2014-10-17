#Everything is a resource in Tasty Pie
from tastypie.resources import ModelResource
#Allows us to set the query types from our models
from tastypie.constants import ALL
from models import Article


class ArticleResource(ModelResource):

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = { "title" : ALL }


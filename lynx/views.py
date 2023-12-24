from django.shortcuts import render,HttpResponse

from . models import Article
# Create your views here.

def home(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render  (request,'lynx/index.html',context=context)

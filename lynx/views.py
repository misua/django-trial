from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.views.generic import View

from .models import Article

def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'lynx/index.html', context=context)

# @method_decorator(csrf_exempt, name='dispatch')
# class ArticleDeleteView(View):
#     def delete(self, request, pk):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         # return JsonResponse({'status':'success'}, status=200)
#         return render(request, 'lynx/delete.html')

def cancel_delete(request):
    return HttpResponse()

class ArticleDeleteView(View):
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            return render(request, 'lynx/delete.html',{'article':article})
            return JsonResponse({'status':'success'}, status=200)
        except Article.DoesNotExist:
            return JsonResponse({'status':'error'}, status=400)
        
    def post(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('home')
    


from django.shortcuts import render
from .models import Article

def index(request):
    context = {
        "msg": "Hello, Noobs!",
    }
    return render(request, 'home.html', context)


def article_list(request):
    context = {
        "articles": Article.objects.all(),
    }
    return render(request, 'list.html', context)



def article_detail(request, article_id):
    context = {
        "article": Article.objects.get(id=article_id),
    }
    return render(request, 'detail.html', context)
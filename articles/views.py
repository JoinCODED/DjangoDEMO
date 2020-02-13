from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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


def article_create(request):
    form = ArticleForm()
    if request.method == "POST":
        print(request.POST)
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form": form
    }
    return render(request, "create.html", context)

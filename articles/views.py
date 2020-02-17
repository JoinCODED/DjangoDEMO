from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def index(request):
    context = {
        "msg": "Hello, World!",
    }
    return render(request, 'home.html', context)


def profile(request):
    return render(request, "profile.html")


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
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("list")
    context = {
        "form": form
    }
    return render(request, "create.html", context)


def article_update(request, article_id):
    article = Article.objects.get(id=article_id)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form": form,
        "article": article
    }
    return render(request, "update.html", context)


def article_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect("list")

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.set_password(user_obj.password)
            user_obj.save()
            login(request, user_obj)
            return redirect("list")
    context = {
        "form": RegisterForm,
    }
    return render(request, 'register.html', context)

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            my_username = form.cleaned_data['username']
            my_password = form.cleaned_data['password']
            user_obj = authenticate(
                username=my_username,
                password=my_password
            )
            if user_obj is not None:
                login(request, user_obj)
                messages.success(request, 'YAY')
                return redirect('list')
            messages.warning(request, 'You shall not pass')
    context = {
        "form":form,
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    messages.warning(request, "We're so sad to see you go :(")
    return redirect("login")

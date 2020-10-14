from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    context = {
        'articles': articles
    }
    return render(request, 'articles/article_list.html', context)

def article_detail(request, slug):
    article = Article.objects.get(slug = slug)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detail.html', context)

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:article-list')
    else:
        form = CreateArticle()
    context = {
        'form': form
    }
    return render(request, 'articles/article_create.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime,time
from django.utils.timezone import make_aware


def index(request):
    # article =Article.objects.get(title__exact='python3')
    # print(article)
    # article_1 =Article.objects.filter(id__exact=1)
    # # article_1 =Article.objects.filter(title__exact=None)
    # print(article_1)
    # print(article_1.query)
    # article = Article.objects.filter(title__iexact='python3')
    # print(article.query)
    # print(article)
    return HttpResponse("success")

def index1(request):
    # article = Article.objects.get(pk=1)
    # article_1 = Article.objects.filter(id=1)
    # print(type(article))
    # print(type(article_1))
    return HttpResponse("success")

def index2(request):
    """icontains大文字小文字区別しない"""
    """contains大文字小文字区別する"""
    result = Article.objects.filter(title__icontains='python')
    print(result.query)
    print(result)
    return HttpResponse("success")

def index3(request):

    # articles = Article.objects.filter(id__in=[1, 2, 3])
    # for article in articles:
    #     print(article)

    # categorys = Category.objects.filter(article__id__in=[
    #     1, 2, 3
    # ])
    # for category in categorys:
    #     print(category)

    # articles = Article.objects.filter(title__icontains='pyth')
    #
    # categories = Category.objects.filter(article__in=articles)
    #
    # for category in categories:
    #     print(category)
    return HttpResponse('success')

def index4(request):
    #id>2のすべての文章を探す
    #gt:greater than より大き
    #gte:greater than erqal　大きか等しい
    #lt:lower than より小さい
    # articles = Article.objects.filter(id__lt=2)
    # print(articles)
    # print(articles.query)
    return HttpResponse('success')

def index5(request):
    """istartswith 大文字小文字区別しないで探す,先端文字が何々である"""
    """startswith 大文字小文字区別するで探す,先端文字が何々である"""
    # articles = Article.objects.filter(title__istartswith='p')
    # print(articles)
    # print(articles.query)
    """endswith ある値で終わり、大文字小文字区別"""
    """iendswith ある値で終わり、大文字小文字区別しない"""
    articles = Article.objects.filter(title__endswith='a')
    print(articles)
    print(articles.query)

    return HttpResponse('success')

def index6(request):
    # article = Article(title='java', content='java_content')
    # article.save()
    # start =make_aware(datetime(year=2019, month=2, day=6, hour=2, minute=0, second=0))
    # end_time =make_aware(datetime(year=2019, month=2, day=6, hour=18, minute=0, second=0))
    """range 二つの時間の間を探す"""
    # articles = Article.objects.filter(create_time__range=(start, end_time))
    # print(articles)
    # print(articles.query)
    return HttpResponse('success')

def index7(request):
    """時間を使った検索"""
    # articles = Article.objects.filter(create_time__date=datetime(year=2019, month=2, day=6))
    # print(articles.query)
    # print(articles)

    """年分だけを使った検索"""
    # articles = Article.objects.filter(create_time__year__gte=2018)
    # print(articles.query)
    # print(articles)

    """曜日検索 4は水曜日"""
    # articles = Article.objects.filter(create_time__week_day=4)
    # print(articles.query)
    # print(articles)

    """時間分秒を入れての検査"""
    # start_time = time(hour=23, minute=40, second=14)
    # end_time = time(hour=1, minute=40, second=15)
    # # articles = Article.objects.filter(create_time__time=time(hour=10, minute=40, second=14))
    # articles = Article.objects.filter(create_time__time__range=(start_time, end_time))
    # print(articles.query)
    # print(articles)

    return HttpResponse('success')

def index8(request):
   """値はnullのデータを探す"""
   # articles = Article.objects.filter(create_time=None)

   """値はnullじゃないの探す"""
   # articles = Article.objects.filter(create_time__isnull=False)

   """正規表現で探す"""
   """regex大文字小文字区別"""
   """iregex大文字小文字区別しない"""
   articles = Article.objects.filter(title__regex=r"^p")

   print(articles.query)
   print(articles)
   return HttpResponse('index8')
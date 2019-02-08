from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Publisher, BookOrder
from django.db.models import Avg,Count,Max,Min,Sum,F
from django.db import connection

def index(request):

    """書籍の平均価格を取得"""
    result = Book.objects.aggregate(avg=Avg('price'))
    print(result)

    print(connection.queries)
    return HttpResponse("sucess")


def index2(request):
    """aggregate一つのdict戻る"""
    # result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    # print(result)
    # print(connection.queries)

    """annotate"""
    # books = Book.objects.annotate(avg=Avg("bookorder__price"))
    # for book in books:
    #     print('%s/%s' % (book.name, book.avg))

    return HttpResponse('index2')

def index3(request):
    """Count"""
    # counts = Book.objects.aggregate(book_nums=Count('id'))
    # print(counts)
    # print(connection.queries)

    """Count.distinct->複数ある値を無視"""
    # result = Author.objects.aggregate(count=Count('email',
    #                                               distinct=True))
    # print(result)
    # print(connection.queries)

    """本ごとの販売数を求む"""
    # results = Book.objects.annotate(count=Count("bookorder__book_id"))
    # for result in results:
    #     print('%s/%s冊' % (result.name, result.count))
    # print(connection.queries)
    return HttpResponse("index3")

def index4(request):
    # author = Author.objects.aggregate(max=Max('age'), min=Min('age'))
    # print(author)
    # print(connection.queries)

    # book = Book.objects.aggregate(max=Max('bookorder__price'))
    # print(book)
    """本販売時の最大価額と最小価額"""
    # books = Book.objects.annotate(max=Max('bookorder__price'), min=Min('bookorder__price'))
    # for book in books:
    #     print('%s/%s/%s' % (book.name, book.max, book.min))

    return HttpResponse("index3")

def index5(request):
    """一つのカラムの値合計値を求む"""
    # book = Book.objects.aggregate(sum=Sum('price'))
    # print(book)

    """各本どのくらい売れてるかの値"""
    # books = Book.objects.annotate(sum=Sum("bookorder__price"))
    # for book in books:
    #     print('%s/%s'%(book.name,book.sum))

    """2.2019年本の総販売量"""
    # books = Book.objects.filter(
    #     bookorder__create_time__year=2019).aggregate(total=Sum('price'))
    # print(books)

    """2.2019年各本の総販売量"""
    # books = Book.objects.filter(bookorder__create_time__year=2019).annotate(total=Sum('bookorder__price'))
    # for book in books:
    #     print('%s/%s'%(book.name,book.total))

    return HttpResponse('index5')

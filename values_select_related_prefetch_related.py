from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,BookOrder
from django.db import connection
from django.db.models import Q,F,Count,Avg,Prefetch

def index4(request):
    """valuesはリストとして返ってくる"""
    """authorname=F('author__name') カラム名を再定義,だけど元のテーブルにあるカラム名と一致してはいけない"""
    # books = Book.objects.values("id", "name", authorname=F('author__name'))
    # for book in books:
    #     print(book)
    """id,name,各どのくらい売れたのか"""
    # books = Book.objects.values("id", "name", order_nums=Count("bookorder"))
    # for book in books:
    #      print(book)

    """values_listはタプルで返ってくる"""
    """flat=True """
    # books = Book.objects.values_list("id", 'name', 'author__name')
    """一つのカラムを取得する場合 flat=True で()をぬける"""
    books = Book.objects.values_list('name', flat=True)
    for book in books:
        print(book)
    return HttpResponse('index4')

def index5(request):
    """all()方法"""
    books = Book.objects.all()
    print(books.query)
    for book in books:
        print(book.id, book.name, book.price)
    return HttpResponse('index5')

def index6(request):
    """select_related"""
    """伝統方法でbook関連してる作者名を探し出す"""
    # books = Book.objects.all()

    """select_related方法"""
    """sqlの効率化,関連モデル使うと分かったら,先に探し出す"""
    """多対一の場合しか使えない"""
    books = Book.objects.select_related("author", 'publisher')
    for book in books:
        print(book.author.name)
        print(book.publisher.name)
    print(connection.queries)
    return HttpResponse('index6')

def index7(request):
    """書籍の名前と注文idを取得"""
    # books =Book.objects.all()
    # for book in books:
    #     print('='*30)
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)
    # print()

    """書籍の名前と注文idを取得"""
    # books = Book.objects.annotate(count=Count("bookorder__book_id"))
    # for book in books:
    #     print('=' * 30)
    #     print(book.name,'の注文数は:',book.count)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)

    """prefetch_related方法"""
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print('=' * 30)
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)
    # print(connection.queries)

    # books = Book.objects.prefetch_related('author')
    # for book in books:
    #         print(book.name,book.author.name)
    # print(connection.queries)

    """本の名前と注文数かつ値段を2500"""
    """伝統方法"""
    # books = Book.objects.all()
    # for book in books:
    #     print('='*30)
    #     print(book.name)
    #     pricees = book.bookorder_set.filter(price__gte=2500)
    #     for pricee in pricees:
    #         print(pricee.price)
    """Prefetch方法 + prefetch_related"""
    prefetch = Prefetch("bookorder_set",
                        queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print('='*30)
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)



    return HttpResponse('index7')
from django.db.models import Avg,Count,Max,Min,Sum,F

def index6(request):
    """F式"""
    """金額全てある価額増やす"""
    """一般方法"""
    # books = Book.objects.all()
    # for book in books:
    #     book.price += 10
    #     book.save()

    """f表現式"""
    # Book.objects.update(price=F("price")+10)
    # print(connection.queries[-1])

    """名前とemail同じのを見つける"""
    # authors = Author.objects.filter(name=F("email"))
    # for author in authors:
    #     print(author.name, author.email)

    return HttpResponse("index6")

def index7(request):
    """Q式"""
    """伝統方法"""
    """値段2000以上かつ評価4.8以上"""
    # books = Book.objects.filter(price__gte=2000, rating__gte=4.8)
    # for book in books:
    #     print(book.name, book.price, book.rating)
    # print(books.query)
    """Q式方法"""
    """値段2000以上かつ評価4.8以上"""
    # books = Book.objects.filter(Q(price__gte=2000) & Q(rating__gte=4.8))
    # for book in books:
    #     print(book.name, book.price, book.rating)
    # print(books.query)

    """Q式方法"""
    """値段2000以上又は評価4.5以上"""
    # books = Book.objects.filter(Q(price__gte=2000) | Q(rating__gte=4.5))
    # for book in books:
    #     print(book.name, book.price, book.rating)
    # print(books.query)

    """値段2000以上かつタイトルに'入門'を含む"""
    # books = Book.objects.filter(Q(price__gte=2000) & Q(name__icontains='入門'))
    # for book in books:
    #   print(book.name, book.price, book.rating)

    """値段2500以上'はじめて'含めていないもの"""
    """       ~を入れると反対選択になる           """
    books = Book.objects.filter(Q(price__gte=2500) & ~Q(name__icontains='はじめて'))
    for book in books:
      print(book.name, book.price, book.rating)

    return HttpResponse("index7")



def index2(request):
    """id>2の本"""
    # books = Book.objects.filter(id__gte=2)

    """id !=3 の本"""
    # books =Book.objects.filter(~Q(id=3))

    """[filter(~Q(id=3))] id >= 2 && id != 3  链式调用"""
    # books = Book.objects.filter(id__gte=2).filter(~Q(id=3))

    """[exclude]条件付きで排除"""
    # books = Book.objects.filter(id__gte=2).exclude(id=3)

    """本を選択してかつ作者名を結果に追加"""
    # books = Book.objects.filter(id=2).annotate(author_name=F('author__name'))
    # for boos in books:
    #     print(boos.name,boos.author_name)
    """本と作者を表示"""
    books = Book.objects.annotate(author_name=F('author__name'))
    for book in books:
     print(book.name, book.author_name)

    print(connection.queries)
    return HttpResponse('index2')

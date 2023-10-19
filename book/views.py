from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from utils.app import *

# Create your views here.


@api_view(["GET"])
def probidhan_search_book(request, years):
    try:
        get_probidhan = Probidhan.objects.get(probidhan_years=years)
        all_books = AllBook.objects.filter(probidhan=get_probidhan)
        all_books_data_serializer = AllBookSerializer(all_books, many=True)
        all_books_data = all_books_data_serializer.data
        return respons_setup('get all address', all_books_data, 200)

    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def publisher_search_book(request, id):
    try:
        get_publisher = BookPublisher.objects.get(id=id)
        all_books = AllBook.objects.filter(book_publisher=get_publisher)
        all_books_data_serializer = AllBookSerializer(all_books, many=True)
        all_books_data = all_books_data_serializer.data
        return respons_setup('get all address', all_books_data, 200)

    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def books(request):
    try:
        all_books = AllBook.objects.all()
        all_books_data_serializer = AllBookSerializer(all_books, many=True)
        all_books_data = all_books_data_serializer.data
        return respons_setup('get all address', all_books_data, 200)
    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def single_books(request, id):
    try:
        get_books = AllBook.objects.get(id=id)
        book_data_serializer = AllBookSerializer(get_books)
        book_data = book_data_serializer.data
        return respons_setup('get all address', book_data, 200)

    except Exception as error:
        return respons_setup('there was an servier said error', {}, 400)


@api_view(["GET"])
def book_chapter_pages(request, chapter):
    try:
        get_chapter = Chapter.objects.get(id=chapter)
        all_pages = Page.objects.filter(chapter=get_chapter)

        all_pages_data_serializer = PageSerializer(all_pages, many=True)
        all_pages_data = all_pages_data_serializer.data
        print(all_pages_data)
        return respons_setup('get all address', all_pages_data, 200)

    except Exception as error:
        print(error)
        return respons_setup('there was an servier said error', {}, 400)

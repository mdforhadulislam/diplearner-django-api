from django.urls import path, include
from .views import *
from knox import views as knox_views
from book.views import *

urlpatterns = [
    path('', getApiUrls),

    path('auth/login/', login, name='login'),
    path('auth/register/', register, name='register'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('accounts/<str:id>/', user_info, name='user_info'),

    path('address/', address, name='address'),
    path('address/regions/', region, name='region'),
    path('address/regions/citys', city, name='city'),
    path('address/regions/citys/areas', area, name='area'),

    path('books/', books, name='books'),
    path('books/<str:id>/', single_books, name='single_books'),
    path('books/<str:chapter>/pages/', book_chapter_pages, name='books_pages'),

    path('probidhan/<str:years>', probidhan_search_book,
         name='all_same_probidhan_books'),
    path('publisher/<str:id>', publisher_search_book,
         name='all_same_publisher_books'),

]

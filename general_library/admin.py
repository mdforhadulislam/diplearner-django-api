from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(LibraryBookPublisher)
admin.site.register(LibraryBook)
admin.site.register(BookChapter)
admin.site.register(BookPage)


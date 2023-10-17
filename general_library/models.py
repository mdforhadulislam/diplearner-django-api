
from django.db import models

# Create your models here.


class LibraryBookPublisher(models.Model):
    publisher_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.publisher_name

class LibraryBook(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    book_publisher = models.ForeignKey(LibraryBookPublisher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.book_publisher}'


class BookChapter(models.Model):
    book = models.ForeignKey(LibraryBook, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=100, blank=True, null=True)
    chapter_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.chapter_name} - {self.chapter_number}'


class BookPage(models.Model):
    book = models.ForeignKey(LibraryBook, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100, blank=True, null=True)
    chapter = models.ForeignKey(BookChapter, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=100, blank=True, null=True)
    page_number = models.CharField(max_length=100, blank=True, null=True)
    page_images = models.ImageField(
        upload_to='page/', blank=True, null=True)

    def __str__(self):
        return f'{self.book_name} - {self.chapter_name} - {self.page_number}'
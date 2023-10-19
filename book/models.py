from django.db import models

# Create your models here.


class Probidhan(models.Model):
    probidhan_years = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.probidhan_years


class BookPublisher(models.Model):
    publisher_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.publisher_name



class Chapter(models.Model):
    chapter_name = models.CharField(max_length=100, blank=True, null=True)
    chapter_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.chapter_name} - {self.chapter_number}'



class AllBook(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    probidhan = models.ForeignKey(Probidhan, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=7, blank=True, null=True)
    book_publisher = models.ForeignKey(BookPublisher, on_delete=models.CASCADE)
    chapter = models.ManyToManyField(Chapter,blank=True)

    def __str__(self):
        return f'{self.name} - {self.subject_code} - {self.probidhan} - {self.book_publisher}'



class Page(models.Model):
    book_name = models.CharField(max_length=100, blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=100, blank=True, null=True)
    page_number = models.CharField(max_length=100, blank=True, null=True)
    page_images = models.ImageField(
        upload_to='page/', blank=True, null=True)

    def __str__(self):
        return f'{self.book_name} - {self.chapter_name} - {self.page_number}'

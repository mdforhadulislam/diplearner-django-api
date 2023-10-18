from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import *


class LibraryBookPublisherSerializer(serializers.Serializer):
    publisher_name = serializers.CharField(max_length=100)

    class Meta:
        model = LibraryBookPublisher
        field = '__all__'


class LibraryBookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    book_publisher = LibraryBookPublisherSerializer(read_only=True)

    class Meta:
        model = LibraryBook
        field = '__all__'


class BookChapterSerializer(serializers.Serializer):
    book = LibraryBookSerializer(read_only=True)
    chapter_name = serializers.CharField(max_length=100)
    chapter_number = serializers.CharField(max_length=100)

    class Meta:
        model = BookChapter
        field = '__all__'


class BookPageSerializer(serializers.Serializer):
    book = LibraryBookSerializer(read_only=True)
    book_name = serializers.CharField(max_length=100)
    chapter = BookChapterSerializer(read_only=True)
    chapter_name = serializers.CharField(max_length=100)
    page_number = serializers.CharField(max_length=100)
    page_images = serializers.ImageField()

    class Meta:
        model = BookPage
        field = '__all__'

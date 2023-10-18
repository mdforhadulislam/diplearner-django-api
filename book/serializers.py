from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import *


class ProbidhanSerializer(serializers.Serializer):
    probidhan_years = serializers.CharField(max_length=5)

    class Meta:
        model = Probidhan
        field = '__all__'


class BookPublisherSerializer(serializers.Serializer):
    publisher_name = serializers.CharField(max_length=100)

    class Meta:
        model = BookPublisher
        field = '__all__'


class AllBookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    probidhan = ProbidhanSerializer(read_only=True)
    subject_code = serializers.CharField(max_length=7)
    book_publisher = BookPublisherSerializer(read_only=True)

    class Meta:
        model = AllBook
        field = '__all__'


class ChapterSerializer(serializers.Serializer):
    book = AllBookSerializer(read_only=True)
    chapter_name = serializers.CharField(max_length=100)
    chapter_number = serializers.CharField(max_length=100)

    class Meta:
        model = AllBook
        field = '__all__'


class PageSerializer(serializers.Serializer):
    book = AllBookSerializer(read_only=True)
    book_name = serializers.CharField(max_length=100)
    chapter = ChapterSerializer(read_only=True)
    chapter_name = serializers.CharField(max_length=100)
    page_number = serializers.CharField(max_length=100)
    page_images = serializers.ImageField()

    class Meta:
        model = AllBook
        field = '__all__'

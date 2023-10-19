from django.contrib.auth.models import User
from rest_framework import serializers, validators
from .models import *


class ProbidhanSerializer(serializers.ModelSerializer):
    probidhan_years = serializers.CharField(max_length=5)

    class Meta:
        model = Probidhan
        fields = '__all__'


class BookPublisherSerializer(serializers.ModelSerializer):
    publisher_name = serializers.CharField(max_length=100)

    class Meta:
        model = BookPublisher
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    chapter_name = serializers.CharField(max_length=100)
    chapter_number = serializers.CharField(max_length=100)

    class Meta:
        model = Chapter
        fields = '__all__'


class AllBookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    probidhan = ProbidhanSerializer(read_only=True)
    subject_code = serializers.CharField(max_length=7)
    book_publisher = BookPublisherSerializer(read_only=True)
    chapter = ChapterSerializer(many=True)

    class Meta:
        model = AllBook
        fields = ('__all__')


class PageSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(max_length=100)
    chapter = ChapterSerializer(read_only=True)
    chapter_name = serializers.CharField(max_length=100)
    page_number = serializers.CharField(max_length=100)
    page_images = serializers.ImageField()

    class Meta:
        model = AllBook
        fields = ('id','page_images', 'chapter','book_name', 'chapter_name', 'page_number')

# Generated by Django 4.2.6 on 2023-10-19 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('subject_code', models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookPublisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(blank=True, max_length=100, null=True)),
                ('chapter_number', models.CharField(blank=True, max_length=100, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.allbook')),
            ],
        ),
        migrations.CreateModel(
            name='Probidhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probidhan_years', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=100, null=True)),
                ('chapter_name', models.CharField(blank=True, max_length=100, null=True)),
                ('page_number', models.CharField(blank=True, max_length=100, null=True)),
                ('page_images', models.ImageField(blank=True, null=True, upload_to='page/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.allbook')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='allbook',
            name='book_publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookpublisher'),
        ),
        migrations.AddField(
            model_name='allbook',
            name='probidhan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.probidhan'),
        ),
    ]

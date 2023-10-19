# Generated by Django 4.2.6 on 2023-10-19 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general_library', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile_image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('mobile_number', models.CharField(blank=True, max_length=12, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], default=' ', max_length=20, null=True)),
                ('institute_name', models.CharField(blank=True, max_length=200, null=True)),
                ('area_address', models.TextField(blank=True, max_length=500, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('bying_book', models.ManyToManyField(blank=True, to='book.allbook')),
                ('bying_genaral_book', models.ManyToManyField(blank=True, to='general_library.librarybook')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city'),
        ),
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.region'),
        ),
    ]

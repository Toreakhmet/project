# Generated by Django 4.2.5 on 2023-10-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taraz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sea', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images_sea/')),
                ('size_sez', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]

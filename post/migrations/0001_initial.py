# Generated by Django 5.0.6 on 2024-06-12 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authors', '0001_initial'),
        ('catagories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=64)),
                ('content', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authors.authors')),
                ('category', models.ManyToManyField(to='catagories.catagories')),
            ],
        ),
    ]
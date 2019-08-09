# Generated by Django 2.2 on 2019-07-21 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import goodmenu.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='One Line Description')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Goodmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(default='강동', max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('smallbody', models.CharField(max_length=500, null=True)),
                ('body', models.TextField(null=True)),
                ('visitcount', models.IntegerField(default=0)),
                ('likecount', models.IntegerField(default=0)),
                ('star', models.IntegerField(default=3)),
                ('smallimg', goodmenu.fields.ThumbnailImageField(upload_to='goodmenu/%Y/%m')),
                ('detailimg', goodmenu.fields.ThumbnailImageField(upload_to='goodmenu/%Y/%m')),
                ('location', goodmenu.fields.ThumbnailImageField(upload_to='goodmenu/%Y/%m')),
                ('url', models.URLField(null=True, verbose_name='url')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('open_time', models.DateTimeField()),
                ('close_time', models.DateTimeField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodmenu.Album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

# Generated by Django 2.2 on 2019-08-03 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usermenu', '0011_userstar_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('userauthorcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userauthorcomment', to=settings.AUTH_USER_MODEL)),
                ('usermenucomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usermenucomment', to='usermenu.UserMenu')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='usercomment',
            name='usermenu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usermenucomment', to='usermenu.UserMenu'),
        ),
    ]
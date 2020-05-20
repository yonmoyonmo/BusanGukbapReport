# Generated by Django 3.0.6 on 2020-05-20 13:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_resized.forms
import report.models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20200520_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 5, 20, 13, 2, 5, 587049, tzinfo=utc))),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('thumbnail', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[960, 540], upload_to=report.models.user_path)),
                ('fullshot', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[960, 540], upload_to=report.models.user_path)),
                ('fullshot_caption', models.CharField(max_length=200)),
                ('detailshot', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[960, 540], upload_to=report.models.user_path)),
                ('detailshot_caption', models.CharField(max_length=200)),
                ('menushot', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[960, 540], upload_to=report.models.user_path)),
                ('menushot_caption', models.CharField(max_length=200)),
                ('youtubelink', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('gukmool', models.IntegerField()),
                ('gogi', models.IntegerField()),
                ('kimchi', models.IntegerField()),
                ('service', models.IntegerField()),
                ('weesaeng', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 5, 20, 13, 2, 5, 586050, tzinfo=utc)),
        ),
    ]
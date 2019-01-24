# Generated by Django 2.1.5 on 2019-01-22 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20190122_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='videos.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Video private'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Video name'),
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Video views'),
        ),
    ]
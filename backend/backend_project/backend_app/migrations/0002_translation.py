# Generated by Django 3.0.6 on 2020-05-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_text', models.CharField(max_length=60)),
                ('target_text', models.CharField(max_length=60)),
                ('unique', models.CharField(max_length=60)),
            ],
        ),
    ]

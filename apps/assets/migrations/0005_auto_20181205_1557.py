# Generated by Django 2.1.3 on 2018-12-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20181204_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'Tag标签',
                'verbose_name_plural': 'Tag标签',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='assets.Tag'),
        ),
    ]

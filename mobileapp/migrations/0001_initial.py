# Generated by Django 3.0.5 on 2020-08-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('count', models.IntegerField(default=0, verbose_name='Кол-во продукта')),
                ('purchase_date', models.DateField(verbose_name='Дата покупки')),
            ],
        ),
    ]

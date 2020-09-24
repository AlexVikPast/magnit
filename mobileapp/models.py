from django.db import models


# Create your models here.
class Products(models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    count = models.IntegerField(default=0, verbose_name='Кол-во продукта')
    purchase_date = models.DateField(verbose_name='Дата покупки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
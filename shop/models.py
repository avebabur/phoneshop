from django.db import models


class Rubric(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


class Phone(models.Model):
    name = models.CharField('Название', max_length=100)
    body = models.TextField('Описание')
    date = models.DateField('Дата релиза')
    boolean = models.BooleanField('Доступность')
    price = models.FloatField('Цена')
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT)
    image = models.ImageField('Фото')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'
        ordering = '-date',
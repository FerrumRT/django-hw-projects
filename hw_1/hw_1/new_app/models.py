from django.db import models


# Create your models here.
class MyModel(models.Model):
    my_field = models.IntegerField()
    is_my_field = models.BooleanField()
    name_field = models.CharField(max_length=50)
    date_field = models.DateField()

    class Meta:
        verbose_name = 'Моделька'
        verbose_name_plural = 'Модельки'

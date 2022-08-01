from django.db import models
from django.db import connection


class Supply(models.Model):
    """
    Модель таблицы поставок.
    order - номер заказа
    price_usd - цена в долларах
    price_rur - цена в российских рублях
    supply_date - срок поставки
    """
    number_pos = models.AutoField(primary_key=True)
    order = models.IntegerField()
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    price_rur = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    supply_date = models.DateField()

    def __str__(self):
        return str(self.order)

    class Meta:
        db_table = 'supplies'



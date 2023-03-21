from django.db import models


class Pets(models.Model):
    cat = models.ForeignKey('Category', related_name='categ', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    photo = models.URLField(default=None, blank=True)
    type = models.ForeignKey('TypeOf', related_name='type', on_delete=models.PROTECT)
    status = models.ForeignKey('StatusOF', related_name='stat', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    category_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.category_id)


class TypeOf(models.Model):
    typet = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип'

    def __str__(self):
        return str(self.typet)


class StatusOf(models.Model):
    statuspet = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Статус'

    def __str__(self):
        return str(self.statuspet)


class OrderOf(models.Model):
    ordernum = models.ForeignKey(Pets, null=True, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    datetime = models.DateTimeField(default=None)
    ordstatus = models.ForeignKey('OrderStatus', null=True, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.ordstatus)


class OrderStatus(models.Model):
    statord = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Статус Заказа'
        verbose_name_plural = 'Статус Заказов'

    def __str__(self):
        return str(self.statord)

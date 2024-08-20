from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    sort = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    COLOR_CHOICES = [
        ('красный', 'Красный'),
        ('синий', 'Синий'),
        ('зеленый', 'Зеленый'),
        ('желтый', 'Желтый'),
        ('черный', 'Черный'),
        ('белый', 'Белый'),
    ]

    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

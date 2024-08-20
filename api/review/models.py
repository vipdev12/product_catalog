from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ..product.models import Product
# Create your models here.


class Review(models.Model):
    body = models.TextField()
    rate = models.IntegerField(choices=[(i, str(i)) for i in range(6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'Отзыв от {self.user.username} для {self.product.title}'

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


User = get_user_model()


class Review(models.Model):
    text = models.TextField(verbose_name="Текст отзыва")
    author = models.CharField(max_length=100, verbose_name="Автор")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.author}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

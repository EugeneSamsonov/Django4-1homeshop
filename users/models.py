from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users/images', blank=True, null=True, verbose_name="Аватар")
    

    class Meta:
        db_table = 'user'
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"
        ordering = ("id", )
    

    def __str__(self) -> str:
        return self.username
    
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя категории")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")


    class Meta:
        db_table = 'category'
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
    

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя продукта")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='goods/images', blank=True, null=True, verbose_name="Изображение")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Колличество")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Категория")
    

    class Meta:
        db_table = 'product'
        verbose_name = "продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id", )
    

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"
    
    def show_correct_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        
        return self.price
    
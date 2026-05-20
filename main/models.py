from django.db import models


class ProductCategory(models.TextChoices):
    MEAT = "meat", "Go'sht"
    RICE = "rice", "Guruch"
    MILK = "milk", "Sut mahsulotlari"


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20,
        choices=ProductCategory.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def __str__(self):
        return self.name


class MonthlyPrice(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="prices"
    )

    year = models.PositiveIntegerField()
    month = models.PositiveSmallIntegerField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["year", "month"]
        unique_together = ("product", "year", "month")
        verbose_name = "Oylik narx"
        verbose_name_plural = "Oylik narxlar"

    def __str__(self):
        return f"{self.product.name} - {self.month}/{self.year}"
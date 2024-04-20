from django.db import models


# Create your models here.
class ClothCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ClothManufacturerModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ClothModel(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(ClothManufacturerModel, on_delete=models.CASCADE)
    category = models.ManyToManyField(ClothCategoryModel)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to="images/")

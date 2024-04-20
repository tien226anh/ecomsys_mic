from django.db import models


# Create your models here.
class BookCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class PublisherModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(AuthorModel)
    publisher = models.ManyToManyField(PublisherModel)
    category = models.ManyToManyField(BookCategoryModel)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    published_date = models.DateField()
    cover_url = models.ImageField(upload_to="covers/")

    def __str__(self):
        return self.title

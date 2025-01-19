from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images", default="images/bg.jpg", blank=True)
    isActive = models.BooleanField(default=0, null=0)
    slug = models.SlugField(default="", null=0, unique=True)
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name} {self.price}"
    

class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")
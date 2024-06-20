from django.db import models

class Product(models.Model):
    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
        ('Nintendo', 'Nintendo'),
        ('PlayStation', 'PlayStation'),
    ]

    CONDITION_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Console(models.Model):
    TYPE_CHOICES = [
        ('Portátil', 'Portátil'),
        ('Hogar', 'Hogar'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='consoles/', blank=True, null=True)

    def __str__(self):
        return self.name

class Accessory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='accessories/', blank=True, null=True)

    def __str__(self):
        return self.name

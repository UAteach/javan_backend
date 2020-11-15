from django.db import models

# Create your models here.
class Item(models.Model):
    CATEGORY = (
        ('MATH', 'Mathematics'),
        ('CHEM', 'Chemistry'),
        ('BIO', 'Biology'),
        ('HOUSE', 'Household'),
        ('CRAFT', 'Craft'),
        ('PHYS', 'Physics'),
        ('TOY', 'Toy'),
        ('TECH', 'Tech')
    )
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=5, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=10, null=True, blank=True)
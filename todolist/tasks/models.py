from django.db import models
from categories.models import Category
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=20)
    due_date = models.DateField()
    
    category = models.ManyToManyField(Category)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
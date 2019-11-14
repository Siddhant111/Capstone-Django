from django.db import models

# Create your models here.

class Document(models.Model):
    document = models.ImageField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

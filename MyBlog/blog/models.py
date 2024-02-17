from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now)  # Додаємо значення за замовчуванням

    def __str__(self):
        return self.title

    def published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.pub_date <= now
    published_recently.admin_order_field = 'pub_date'
    published_recently.boolean = True
    published_recently.short_description = 'Published recently?'
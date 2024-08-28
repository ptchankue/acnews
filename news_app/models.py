from django.db import models

# Create your models here.


class Article(models.Model):
    link = models.CharField(max_length=100)
    source = models.CharField(max_length=100, blank=True, default="")
    thumbnail = models.CharField(max_length=100, blank=True, default="")
    view_count = models.IntegerField(default=0)
    snippet = models.CharField(max_length=100, blank=True, default="")
    title = models.CharField(max_length=100)
    fetched_on = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Link: {self.link.encode('utf-8')}"


class Visitor(models.Model):
    ip = models.CharField(max_length=100)
    nb_visit = models.IntegerField(default=0)
    last_visit = models.DateTimeField(auto_now=True)

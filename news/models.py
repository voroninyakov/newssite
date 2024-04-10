from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import json
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='news/')
    tags = models.ManyToManyField("Tag", blank=True, related_name='news')
    views = models.IntegerField()
    
    def get_likes_count(self):
        return self.reactions.all().filter(is_like=True).count()
    
    def get_dislikes_count(self):
        return self.reactions.all().filter(is_like=False).count()
    
    def get_absolute_url(self):
        return reverse("news:news_detail", kwargs={"pk": self.pk})
    
    def get_html(self):
        try:
            image = self.image.url
        except ValueError:
            image = None
        html = f"""<article>
        <img src='{image}'>
        <h2><a href="{ self.get_absolute_url }">{self.title}</a></h2>
        <h3>Просмотры: { self.views }</h3><h3>Лайки: { self.get_likes_count() }</h3><h3>Дизлайки: { self.get_dislikes_count() }</h3>
        <ul>"""
        for tag in self.tags.all():
            html += f"<li><a href='{tag.get_absolute_url()}'>{ tag.text }</a></li>"
        html += "</ul></article>"
        return html
        
class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)
    
    def get_absolute_url(self):
        return reverse("news:news_by_tag", kwargs={"pk": self.pk})
    
class Reaction(models.Model):
    news = models.ForeignKey(News, related_name='reactions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reactions', on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)
    
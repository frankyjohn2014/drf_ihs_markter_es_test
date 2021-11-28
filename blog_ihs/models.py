from django.db import models

class User(models.Model):
    full_name = models.CharField(verbose_name='User', db_index=True, max_length=256)
    
    def __str__(self):
                return self.full_name
class Article(models.Model):
    paragraph = models.CharField(verbose_name='Title', db_index=True, max_length=256)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(verbose_name='Date', blank=True)

    def __str__(self):
            return f'{self.author}: {self.paragraph} ({self.created_datetime.date()})'
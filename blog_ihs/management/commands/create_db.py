from django.core.management.base import BaseCommand
from blog_ihs.models import Article,User
import datetime
import lorem
import names
import radar
from django.utils import timezone
from django.test import override_settings
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        my_names_ = []
        for i in range(0,19):
            my_names_.append(names.get_full_name())
        self.stdout.write(self.style.SUCCESS('Started database population process...'))
        for i in range(0,20):
            rnd = random.randint(0, 9)
            User_created = User.objects.create(
                full_name = my_names_[rnd],
            )
            print(i)
            User_created.save()
        for i in range(0,60):
            rnd = random.randint(1, 9)
            web_articles = Article.objects.create(
                paragraph = lorem.sentence(),
                author = User.objects.get(pk=rnd),
                created_datetime = radar.random_datetime(
                    start = datetime.datetime(year=2014, month=1, day=1),
                    stop = datetime.datetime(year=2021, month=1, day=24)
            ))   
            web_articles.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database.'))
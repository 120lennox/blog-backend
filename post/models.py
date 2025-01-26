from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    PREDEFINED_CATEGORIES = [
        ('Leadership', 'Leadership'),
        ('Motivation', 'Motivation'),
        ('Inspiration', 'Inspiration'),
        ('Technology', 'Technology'),
        ('Frameworks', 'Frameworks'),
        ('Design', 'Design'),
        ('Research', 'Research'),
        ('Software Development', 'Software Development'),]
    
    name = models.CharField(max_length=200, choices=PREDEFINED_CATEGORIES, unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    # PREDEFINED_CATEGORIES = [
    #     # ('Leadership', 'Leadership'),
    #     # ('Motivation', 'Motivation'),
    #     # ('Inspiration', 'Inspiration'),
    #     # ('Technology', 'Technology'),
    #     # ('Frameworks', 'Frameworks'),
    #     # ('Design', 'Design'),
    #     # ('Research', 'Research'),
    #     # ('Software Development', 'Software Development'),
    #     'Leadership', 'Motivation', 'Inspiration', 'Technology', 
    #     'Frameworks', 'Design', 'Research', 'Software Development'
    # ]

    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title  
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     # automatically create predefined categories if they dont have any
    #     for category in self.PREDEFINED_CATEGORIES:
    #         Category.objects.get_or_create(name=category)


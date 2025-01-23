from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORIES = [
        ('Leadership', 'Leadership'),
        ('Motivation', 'Motivation'),
        ('Inspiration', 'Inspiration'),
        ('Technology', 'Technology'),
        ('Frameworks', 'Frameworks'),
        ('Design', 'Design'),
        ('Research', 'Research'),
        ('Software Development', 'Software Development'),
    ]

    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.CharField(
        max_length=200,
        choices=CATEGORIES,
        blank=True,
        help_text='Select category'
    )

    def __str__(self):
        return self.title  

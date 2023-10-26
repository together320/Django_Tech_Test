from django.db import models

class Article(models.Model):
    """Article class is used to describe articles written by author, according to regions"""

    #Fields
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, null=True)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True
    )

    def __str__(self):
        return f'{self.title} ({self.id})'
from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=100)
    data = models.DateField(auto_now=True)
    # indexing is true for optimized search
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(30)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

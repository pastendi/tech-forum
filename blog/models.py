from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    # Helper funciton
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # things to display in admin panel
    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    date = models.DateField(auto_now=True)
    # indexing is true for optimized search
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(30)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)

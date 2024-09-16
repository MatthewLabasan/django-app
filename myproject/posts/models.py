from django.db import models

# Create your models here.
# model data: each type of data will have a table
# python class -> migrated to table in the database

class Post(models.Model): # models.Model makes this a model
    # these fields relate to the way you will accept the data in a form, 
    # as well as how it is defined in the db
    title = models.CharField(max_length=75) # this is how we define fields for specific object attributes. see model field ref in docs.
    body = models.TextField() # relates to text area form area.
    slug = models.SlugField() # the defining part of the URl or the Post (ex. ourdomain.com/post/this-is-a-slug-article) -> identifies the object / post
    date = models.DateTimeField(auto_now_add=True) # does not show up in admin bc it is auto
    banner = models.ImageField(default='fallback.png', blank=True)
        # imagefield only works with pillow?
        # blank = true means not requiring images.
        # in admin, it'll also allow you to upload photos!

    # methods -> returns title of the post object is printed
    def __str__(self) -> str:
        return self.title


from django.db import models
 
from django.core.urlresolvers import reverse
 

def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_location, null=True,
                              blank=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    author = models.CharField(max_length=200)
    body = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url():
        return reverse('myblog:detail', kwargs={'id': self.id})


# class marq(models.Model):
#     text=models.TextField()
#     def __str__(self):
#         return self.text

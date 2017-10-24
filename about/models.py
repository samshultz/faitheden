from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = "-updated",

    def __str__(self):
        return self.title

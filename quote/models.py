from django.db import models

class marq(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
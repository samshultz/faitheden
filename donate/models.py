from django.db import models

class Payment(models.Model):

	title = models.CharField(max_length=200, blank=True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
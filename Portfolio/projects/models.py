from django.db import models

class Poem(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	published = models.DateTimeField()

	def __str__(self):
		return self.title
	
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Task(models.Model):
	user = models.ForeignKey(User, related_name='tasks',on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=100)
	description = models.TextField()
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + self.content

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Внешний ключ указывает на модель Post
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + self.content
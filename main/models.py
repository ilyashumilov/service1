from django.db import models

# Create your models here.
class post(models.Model):
    context = models.TextField(max_length=5000)
    def __str__(self):
        return self.context

class comment(models.Model):
    post_id = models.ForeignKey(post, on_delete=models.CASCADE)
    context = models.TextField(max_length=5000)
    # Поле для id комментария на который отвечаем, если коментарий не является ответом поле имеет значение 'x'
    comment_id = models.CharField(max_length=100)

    def __str__(self):
        return self.context
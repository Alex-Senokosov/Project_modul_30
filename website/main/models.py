from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField("Описание")
    time = models.DateTimeField("Время записи",auto_now_add=True)
    def __str__(self):
        return self.title

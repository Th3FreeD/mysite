from django.db import models

# создание таблицы в БД (идентификатор установлен автоматичеки)
class Articles(models.Model):
    #поле заголовка строкового типа с максимальным кол-вом символов - 120
    title = models.CharField(max_length=120)
    #поле поста текстового типа
    post = models.TextField()
    #поле даты публикации с использованием даты
    date = models.DateTimeField()

    def __str__(self):
        return self.title
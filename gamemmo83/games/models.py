from django.db import models

class Gamelist(models.Model):
    name = models.CharField('Название игры', max_length=250)
    link_game = models.CharField('URL игры', max_length=250)
    link_img = models.CharField('URL изображения', max_length=250)
    alt_text = models.CharField('Альтернативный текст', max_length=250)
    discript = models.TextField('Описание игры')
    janr = models.CharField('Жанр игры', max_length=250)
    type = models.CharField('Тип игры', max_length=250)
    osobenosti = models.TextField('Особенности игры')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

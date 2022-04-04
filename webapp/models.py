from django.db import models


STATUS_CHOICES = [('new', 'Новый'), ('moderated', 'Модерированный')]


class Quote(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст')
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name="E-Mail")
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][0])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.pk}. {self.name}: {self.email}'

    class Meta:
        db_table = "Quotes"
        verbose_name = 'Цитата'
        verbose_name_plural = "Цитаты"



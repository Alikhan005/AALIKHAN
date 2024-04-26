from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    city = models.CharField(max_length=100, verbose_name="Город")  # Поле "Город"
    age = models.CharField(max_length=150, verbose_name="Возраст")
    school = models.CharField(max_length=100, verbose_name="Школа")
    course = models.CharField(max_length=100, verbose_name="Курс")
    birthday = models.DateField(null=True, verbose_name="День рождения")
    specialty = models.CharField(max_length=100, verbose_name="Специальность")
    ent_score = models.IntegerField(default=0, verbose_name="Баллы ЕНТ")
    hobby = models.CharField(max_length=100, verbose_name="Хобби")

    def __str__(self):
        return self.name

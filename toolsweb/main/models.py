from django.db import models
from django.contrib import admin

SEL_SEX = [
    ('m','Мужской'),
    ('w','Женский'),
]

SEL_REGION = [
    ('bre','Брестская область'),
    ('vit','Витебская область'),
    ('gom','Гомельская область'),
    ('gro','Гродненская область'),
    ('mio','Минская область'),
    ('mog','Могилёвская область'),
    ('min','Город Минск'),
]

SEL_PEDZAVTYPE = [
    ('g','Гимназия'),
    ('l','Лицей'),
    ('sh','Средняя школа'),
    ('bh','Базовая школа'),
    ('bhs','Базовая школа сад'),
    ('shs','Средняя школа сад'),
    ('ss','Спортивная школа'),
    ('k','Колледж'),
]

SEL_SOC = [
    ('n','Ничего'),
    ('do','Дети на опеке'),
    ('vdd','Воспитаник, приемной семьи детского дома семейного типа'),
    ('di','Дети-инвалиды'),
    ('dgs','Дети нуждающиеся в государственной защите'),
    ('ipr','Индивидуально-профилактическая работа'),
    ('sop','Социально-опасное положение'),
    ('opfr','Особености психофизического развития'),
]

SEL_SOC_FAM = [
    ('p','Полная'),
    ('np','Не полная'),
    ('m','Многодетная'),
    ('ri','Родители-инвалиды'),
    ('rchz','Семья из Чернобыльской зоны'),
    ('b','Беженцы'),
    ('os','Опекунская семья'),
    ('ps','Приемная семья'),
    ('rvdd','Родители воспитатели десткого дома семейного типа'),
]

# Create your models here.
class VospitanikOtryadSmena(models.Model):
    vospitanik = models.ForeignKey(
        'Vospitanik',
        on_delete=models.CASCADE,
        verbose_name="Воспитаник"
    )

    otryad = models.ForeignKey(
        'Otryad',
        on_delete=models.CASCADE,
        verbose_name="Отряд"
    )

    smena = models.ForeignKey(
        'Smena',
        on_delete=models.CASCADE,
        verbose_name="Смена"
    )

    def __str__(self):
        return f"связь #{self.id}"

    class Meta:
        verbose_name_plural = "связи"
        verbose_name = "связь"

class Vospitanik(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True)
    second_name = models.CharField(verbose_name="Фамилия", max_length=255, blank=True)
    third_name = models.CharField(verbose_name="Отчество", max_length=255, blank=True)
    sex = models.CharField(verbose_name="Пол", choices=SEL_SEX, default='m', max_length=1, blank=False)
    birthdate = models.DateField(verbose_name="Дата рождения",blank=False)
    phone = models.CharField(verbose_name="Номер телефона", max_length=25 ,blank=True)
    live_place_full = models.CharField(verbose_name="Место жительства", max_length=255, blank=False)
    region = models.CharField(verbose_name="Регион", choices=SEL_REGION, max_length=3, blank=False)
    is_city = models.BooleanField(verbose_name="Сельская местность")
    ped_zav_full = models.CharField(verbose_name="Название учереждения образования", max_length=255, blank=False)
    ped_zav_type = models.CharField(verbose_name="Тип учреждения образования", choices=SEL_PEDZAVTYPE, max_length=3, blank=False)
    state = models.PositiveIntegerField(verbose_name="Класс", blank=False, default=5)
    order_number = models.CharField(verbose_name="Номер путевки", max_length=255, blank=False)
    order_state = models.CharField(verbose_name="Кем выдана", max_length=255, blank=False)
    soc = models.CharField(verbose_name="Социальная характеристика", choices=SEL_SOC, max_length=4, blank=False)
    soc_fam = models.CharField(verbose_name="Социальная характеристика семии", choices=SEL_SOC_FAM, max_length=4, blank=False)
    
    mother_name_full = models.CharField(verbose_name="Полное имя матери", max_length=255, blank=True)
    mother_work = models.CharField(verbose_name="Место работы матери", max_length=255, blank=True)
    mother_post = models.CharField(verbose_name="Должность матери", max_length=255, blank=True)
    mother_phone = models.CharField(verbose_name="Телефон матери", max_length=25, blank=True)

    father_name_full = models.CharField(verbose_name="Полное имя отца", max_length=255, blank=True)
    father_work = models.CharField(verbose_name="Место работы отца", max_length=255, blank=True)
    father_post = models.CharField(verbose_name="Должность отца", max_length=255, blank=True)
    father_phone = models.CharField(verbose_name="Телефон отца", max_length=25, blank=True)

    coment = models.TextField(verbose_name="Комментарий", blank=True)

    smena = models.ManyToManyField(
        'Smena',
        through='VospitanikOtryadSmena',
        related_name='vospitanik',
        verbose_name="Cмены"
    )

    otryad = models.ManyToManyField(
        'Otryad',
        through='VospitanikOtryadSmena',
        related_name='vospitanik',
        verbose_name="Cмены"
    )

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.third_name} # {self.id}"

    class Meta:
        verbose_name_plural = "воспитаники"
        verbose_name = "воспитаник"

class Otryad(models.Model):
    name = models.CharField(verbose_name="Название отряда", max_length=255, blank=False, default="отряд")
    coment = models.TextField(verbose_name="Комментарий", blank=True)

    def __str__(self):
        return f"{self.name} # {self.id}"
    
    class Meta:
        verbose_name_plural = "отряды"
        verbose_name = "отряд"

class Smena(models.Model):
    name = models.CharField(verbose_name="Название смены", max_length=255, blank=False, default="смена")

    start_date = models.DateField(verbose_name="Дата начала смены",blank=False, null=True)
    end_date = models.DateField(verbose_name="Дата окончания смены",blank=False, null=True)
    is_current = models.BooleanField(verbose_name="Текущая смена", default=False)

    coment = models.TextField(verbose_name="Комментарий", blank=True)

    def __str__(self):
        return f"смена {self.name} # {self.id}"
    
    class Meta:
        verbose_name_plural = "смены"
        verbose_name = "смена"
 
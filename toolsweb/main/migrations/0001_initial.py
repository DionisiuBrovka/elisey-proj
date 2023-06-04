# Generated by Django 4.2.1 on 2023-06-04 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otryad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='отряд', max_length=255, verbose_name='Название отряда')),
                ('coment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'отряд',
                'verbose_name_plural': 'отряды',
            },
        ),
        migrations.CreateModel(
            name='Smena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='смена', max_length=255, verbose_name='Название смены')),
                ('start_date', models.DateField(null=True, verbose_name='Дата начала смены')),
                ('end_date', models.DateField(null=True, verbose_name='Дата окончания смены')),
                ('is_current', models.BooleanField(default=False, verbose_name='Текущая смена')),
                ('coment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'смена',
                'verbose_name_plural': 'смены',
            },
        ),
        migrations.CreateModel(
            name='Vospitanik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('third_name', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('sex', models.CharField(choices=[('m', 'Мужской'), ('w', 'Женский')], default='m', max_length=1, verbose_name='Пол')),
                ('birthdate', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='Номер телефона')),
                ('live_place_full', models.CharField(max_length=255, verbose_name='Место жительства')),
                ('region', models.CharField(choices=[('bre', 'Брестская область'), ('vit', 'Витебская область'), ('gom', 'Гомельская область'), ('gro', 'Гродненская область'), ('mio', 'Минская область'), ('mog', 'Могилёвская область'), ('min', 'Город Минск')], max_length=3, verbose_name='Регион')),
                ('is_city', models.BooleanField(verbose_name='Сельская местность')),
                ('ped_zav_full', models.CharField(max_length=255, verbose_name='Название учереждения образования')),
                ('ped_zav_type', models.CharField(choices=[('g', 'Гимназия'), ('l', 'Лицей'), ('sh', 'Средняя школа'), ('bh', 'Базовая школа'), ('bhs', 'Базовая школа сад'), ('shs', 'Средняя школа сад'), ('ss', 'Спортивная школа'), ('k', 'Колледж')], max_length=3, verbose_name='Тип учреждения образования')),
                ('order_number', models.CharField(max_length=255, verbose_name='Номер путевки')),
                ('order_state', models.CharField(max_length=255, verbose_name='Кем выдана')),
                ('soc', models.CharField(choices=[('n', 'Ничего'), ('do', 'Дети на опеке'), ('vdd', 'Воспитаник, приемной семьи детского дома семейного типа'), ('di', 'Дети-инвалиды'), ('dgs', 'Дети нуждающиеся в государственной защите'), ('ipr', 'Индивидуально-профилактическая работа'), ('sop', 'Социально-опасное положение'), ('opfr', 'Особености психофизического развития')], max_length=4, verbose_name='Социальная характеристика')),
                ('soc_fam', models.CharField(choices=[('p', 'Полная'), ('np', 'Не полная'), ('m', 'Многодетная'), ('ri', 'Родители-инвалиды'), ('rchz', 'Семья из Чернобыльской зоны'), ('b', 'Беженцы'), ('os', 'Опекунская семья'), ('ps', 'Приемная семья'), ('rvdd', 'Родители воспитатели десткого дома семейного типа')], max_length=4, verbose_name='Социальная характеристика семии')),
                ('mother_name_full', models.CharField(blank=True, max_length=255, verbose_name='Полное имя матери')),
                ('mother_work', models.CharField(blank=True, max_length=255, verbose_name='Место работы матери')),
                ('mother_post', models.CharField(blank=True, max_length=255, verbose_name='Должность матери')),
                ('mother_phone', models.CharField(blank=True, max_length=25, verbose_name='Телефон матери')),
                ('father_name_full', models.CharField(blank=True, max_length=255, verbose_name='Полное имя отца')),
                ('father_work', models.CharField(blank=True, max_length=255, verbose_name='Место работы отца')),
                ('father_post', models.CharField(blank=True, max_length=255, verbose_name='Должность отца')),
                ('father_phone', models.CharField(blank=True, max_length=25, verbose_name='Телефон отца')),
                ('coment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'воспитаник',
                'verbose_name_plural': 'воспитаники',
            },
        ),
        migrations.CreateModel(
            name='VospitanikOtryadSmena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otryad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.otryad', verbose_name='Отряд')),
                ('smena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.smena', verbose_name='Смена')),
                ('vospitanik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vospitanik', verbose_name='Воспитаник')),
            ],
            options={
                'verbose_name': 'связь',
                'verbose_name_plural': 'связи',
            },
        ),
        migrations.AddField(
            model_name='vospitanik',
            name='otryad',
            field=models.ManyToManyField(related_name='vospitanik', through='main.VospitanikOtryadSmena', to='main.otryad', verbose_name='Cмены'),
        ),
        migrations.AddField(
            model_name='vospitanik',
            name='smena',
            field=models.ManyToManyField(related_name='vospitanik', through='main.VospitanikOtryadSmena', to='main.smena', verbose_name='Cмены'),
        ),
    ]
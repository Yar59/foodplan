# Generated by Django 4.1.7 on 2023-03-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsite', '0017_alter_tarif_allergy_alter_tarif_preferred_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='breakfast',
            field=models.BooleanField(verbose_name='Включен ли завтрак?'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='dessert',
            field=models.BooleanField(verbose_name='Включен ли десерт?'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='dinner',
            field=models.BooleanField(verbose_name='Включен ли ужин?'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='duration',
            field=models.CharField(choices=[('1', '1 месяц'), ('3', '3 месяца'), ('6', '6 месяцев'), ('12', '12 месяцев')], max_length=2, verbose_name='Длительность подписки'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='lunch',
            field=models.BooleanField(verbose_name='Включен ли обед?'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='persons',
            field=models.PositiveIntegerField(verbose_name='Количество персон'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='preferred_menu',
            field=models.CharField(choices=[('cl', 'Классическое'), ('lc', 'Низкоуглеводное'), ('vg', 'Вегетарианское'), ('kt', 'Кето')], max_length=2, verbose_name='Предпочитаемое меню'),
        ),
    ]

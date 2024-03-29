# Generated by Django 4.1.7 on 2023-03-18 12:16

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('foodsite', '0012_tarif_persons'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='ingredients',
            options={'verbose_name': 'Ингридиент', 'verbose_name_plural': 'Ингридиенты'},
        ),
        migrations.AlterModelOptions(
            name='tarif',
            options={'verbose_name': 'Тариф', 'verbose_name_plural': 'Тарифы'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='ingredients',
            name='quantity',
            field=models.FloatField(default=1.0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='group_food',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mt', 'Мясо'), ('fs', 'Рыба'), ('vt', 'Овощи'), ('fr', 'Фрукты'), ('vegt', 'Вегетарианское'), ('veg', 'Веганское'), ('gf', 'Без глютена'), ('eco', 'ЭКО')], max_length=12, null=True, verbose_name='Входит в группу'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='in_menu',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('cl', 'Классическое'), ('lc', 'Низкоуглеводное'), ('vg', 'Вегетарианское'), ('kt', 'Кето')], max_length=8, null=True, verbose_name='Входит в меню'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='allergy',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('fs', 'Рыба и морепродукты'), ('mt', 'Мясо'), ('cl', 'Зерновые'), ('hn', 'Продукты пчеловодства'), ('nt', 'Орехи и бобовые'), ('mk', 'Молочные продукты')], max_length=12, null=True, verbose_name='Алергия на:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferred_dishes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mt', 'Мясо'), ('fs', 'Рыба'), ('vt', 'Овощи'), ('fr', 'Фрукты'), ('vegt', 'Вегетарианское'), ('veg', 'Веганское'), ('gf', 'Без глютена'), ('eco', 'ЭКО')], max_length=14, null=True, verbose_name='Предпочитаемые блюда'),
        ),
    ]

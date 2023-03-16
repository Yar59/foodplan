# Generated by Django 4.1.7 on 2023-03-16 20:13

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('foodsite', '0009_remove_dish_group_dish_group_food_dish_in_menu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred_menu',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('cl', 'Классическое'), ('lc', 'Низкоуглеводное'), ('vg', 'Вегетарианское'), ('kt', 'Кето')], max_length=2, null=True, verbose_name='Предпочитаемое меню'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='group_food',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mt', 'Мясо'), ('fs', 'Рыба'), ('vt', 'Овощи'), ('fr', 'Фрукты'), ('vegt', 'Вегетарианское'), ('veg', 'Веганское'), ('gf', 'Без глютена'), ('eco', 'ЭКО')], max_length=4, null=True, verbose_name='Входит в группу'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='in_menu',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('cl', 'Классическое'), ('lc', 'Низкоуглеводное'), ('vg', 'Вегетарианское'), ('kt', 'Кето')], max_length=2, null=True, verbose_name='Входит в меню'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='allergen',
            field=models.CharField(blank=True, choices=[('fs', 'Рыба и морепродукты'), ('mt', 'Мясо'), ('cl', 'Зерновые'), ('hn', 'Продукты пчеловодства'), ('nt', 'Орехи и бобовые'), ('mk', 'Молочные продукты')], default='Классическое', max_length=2, verbose_name='Входит в группу алергенов'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='measure',
            field=models.CharField(choices=[('kg', 'килограмм'), ('g', 'грамм'), ('cm', 'сантиметр'), ('pс', 'штука')], max_length=3, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='allergy',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('fs', 'Рыба и морепродукты'), ('mt', 'Мясо'), ('cl', 'Зерновые'), ('hn', 'Продукты пчеловодства'), ('nt', 'Орехи и бобовые'), ('mk', 'Молочные продукты')], max_length=2, null=True, verbose_name='Алергия на:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferred_dishes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mt', 'Мясо'), ('fs', 'Рыба'), ('vt', 'Овощи'), ('fr', 'Фрукты'), ('vegt', 'Вегетарианское'), ('veg', 'Веганское'), ('gf', 'Без глютена'), ('eco', 'ЭКО')], max_length=4, null=True, verbose_name='Предпочитаемые блюда'),
        ),
    ]
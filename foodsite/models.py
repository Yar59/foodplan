from django.db import models


class Ingredients(models.Model):
    title = models.CharField('Наименование', max_length=100, unique=True)
    CHOICES = [('kg', 'kilo'), ('g', 'gramm'),
               ('cm', 'centimeter'), ('pс', 'piece')]
    measure = models.CharField('Единица измерения', max_length=3, choices=CHOICES)
    price = models.FloatField('Ориентировочная цена в руб. за единицу измерения', default=0)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField('Имя', max_length=250, default='some_user')
    email = models.EmailField('Адрес электронной почты', max_length=50, unique=True)
    password = models.CharField('Пароль', max_length=12)
    is_manager = models.BooleanField('Является ли менеджером?', default=False)
    is_premium = models.BooleanField('Оплачена премиум подписка?', default=False)
    not_used_ingr = models.ManyToManyField(
        Ingredients,
        related_name='not_for_users',
        verbose_name='Блюда с какими ингредиентами не предлагать',
        blank=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField('Название блюда', max_length=100, unique=True)
    image = models.ImageField('Фото', upload_to='media/', blank=True, null=True)
    ingredients = models.ManyToManyField(
        Ingredients,
        related_name='dishes',
        verbose_name='Какие ингредиенты используются')
    likes = models.ManyToManyField(
        User,
        related_name='liked_dish',
        verbose_name='Кто лайкнул',
        blank=True)
    dislikes = models.ManyToManyField(
        User,
        related_name='disliked_dish',
        verbose_name='Кто дизлайкнул',
        blank=True)

    def __str__(self):
        return self.title

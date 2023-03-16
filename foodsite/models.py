from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Missing email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, is_staff=True, **extra_fields)


PRODUCT_GROUP = [('mt', 'meet'), ('fs', 'fish'),
                 ('vt', 'vegetable'), ('fr', 'fruit'),
                 ('vegt', 'vegetarian'), ('veg', 'vegan'),
                 ('gf', 'gluten_free'), ('eco', 'eco')]


class Ingredients(models.Model):
    title = models.CharField('Наименование', max_length=100, unique=True)
    CHOICES = [('kg', 'kilo'), ('g', 'gramm'),
               ('cm', 'centimeter'), ('pс', 'piece')]
    measure = models.CharField('Единица измерения', max_length=3, choices=CHOICES)

    def __str__(self):
        return self.title


class Tarif(models.Model):
    breakfast = models.BooleanField('Включен ли завтрак?')
    lunch = models.BooleanField('Включен ли обед?')
    dinner = models.BooleanField('Включен ли ужин?')
    dessert = models.BooleanField('Включен ли десерт?')


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Имя', max_length=250, default='some_user')
    email = models.EmailField('Адрес электронной почты', max_length=50, unique=True)
    is_staff = models.BooleanField('Является ли менеджером?', default=False)
    tarif = models.ForeignKey(Tarif, verbose_name='Оплаченный тариф',
                              related_name='users',
                              on_delete=models.PROTECT, null=True, blank=True)
    preferred_dishes = models.CharField('Предпочитаемые блюда',
                                        max_length=4, choices=PRODUCT_GROUP)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username


class Dish(models.Model):
    title = models.CharField('Название блюда', max_length=100, unique=True)
    image = models.ImageField('Фото', upload_to='media/', blank=True, null=True)
    ingredients = models.ManyToManyField(
        Ingredients,
        related_name='dishes',
        verbose_name='Какие ингредиенты используются')
    price = models.FloatField('Ориентировочная цена в руб. за блюдо', default=0)
    group = models.CharField('Предпочитаемые блюда',
                             max_length=4, choices=PRODUCT_GROUP)
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

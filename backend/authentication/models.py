import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from authentication.managers import UserManager
from actor.models import Actor
from director.models import Director
from video.models import Video

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name="Имя", max_length=64)
    last_name = models.CharField(verbose_name="Фамилия", max_length=64)
    email = models.EmailField(verbose_name="Почта", max_length=64, unique=True)
    photo = models.ImageField(verbose_name="Аватарка", upload_to='users/photos', blank=True)
    
    actor = models.ManyToManyField(verbose_name="Любимые актёры", to=Actor, related_name="user", blank=True)
    director = models.ManyToManyField(verbose_name="Любимые режисёры", to=Director, related_name="user", blank=True)
    video = models.ManyToManyField(verbose_name="Любимые видео", to=Video, related_name="user", blank=True)

    is_active = models.BooleanField(verbose_name="Активирован", default=False)
    is_staff = models.BooleanField(verbose_name="Персонал", default=False)
    is_superuser = models.BooleanField(verbose_name="Администратор", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]
    
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

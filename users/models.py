from django.contrib.auth.models import AbstractUser

# 장고 디폴트에서 가져옴
from django.db import models

# Create your models here.
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    # tuple ()
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    # CharField는 1arg를 가지는데 max_length임. ** 중요! 최대 글자수를 말해. null=True는 비어있어도 괜찮다는거야.
    # form에 변화룰 준거(성별성택)같은걸로는 migration등이 필요하지 않아
    avatar = models.ImageField(null=True. blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
from django.db import models


class TimeStamptedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # abstract Model은 모델이지만 db에 등록되지 않는 모델_코드에서만 쓰임
    class Meta:
        abstract = True
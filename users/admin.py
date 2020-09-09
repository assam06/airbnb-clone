from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# 여기에 추가하는걸로 확장할 수 있어
# 데코레이터는 클래스 위에 있어야 작동해. 얘는 게시판 위에 분류 만들어줌
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin  """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

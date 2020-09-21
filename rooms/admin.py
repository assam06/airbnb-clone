from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                # 접는 섹션을 만들어줌
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )
    # 리스트 정렬문제
    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    # 검색하는 방법 정하기
    search_fields = ("=city", "^host__username")

    # manytomany에서 작동하는 Horizontal...
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    # self는 RoomAdmin class임. 그 자체, obj는 현재의 row
    def count_amenities(self, obj):
        return obj.amenities.count()
        return "Potato"

    count_amenities.short_description = "hello sexy!"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ """

    pass
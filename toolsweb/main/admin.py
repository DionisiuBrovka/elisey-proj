from django.contrib import admin
from .models import *

admin.site.site_header = '"Справка и Учёт" v0.1'
admin.site.site_title = '"Справка и Учёт" v0.1'


# Register your models here.
class ProfilePhotoInline(admin.TabularInline):
    model = VospitanikOtryadSmena
    extra = 0


@admin.register(Vospitanik)
class VospitanikAdmin(admin.ModelAdmin):

    model = Vospitanik

    fieldsets = [
        (
            "Информация о ребенке",
            {
                'fields':["second_name","first_name","third_name","sex","birthdate","phone","soc","soc_fam"]
            }
        ),
        (
            "Информация о путевке",
            {
                'fields':["order_number","order_state"]
            }
        ),
        (
            "Информация о месте жительства",
            {
                'fields':["live_place_full","region","is_city"]
            }
        ),
        (
            "Информация о учебном заведении",
            {
                'fields':["ped_zav_full","ped_zav_type"]
            }
        ),
        (
            "Информация о матери",
            {
                'fields':["mother_name_full","mother_work","mother_post","mother_phone"]
            }
        ),
        (
            "Информация об отце",
            {
                'fields':["father_name_full","father_work","father_post","father_phone"]
            }
        ),
        (
            "Другое",
            {
                'fields':["coment"]
            }
        )
    ]

    list_display = ('id','second_name', 'first_name','third_name','birthdate')
    # list_filter = ('decade_born_in',)

    inlines = [
        ProfilePhotoInline
    ]

    search_fields = ['second_name', 'first_name','third_name']
    list_display_links = ['id','second_name', 'first_name','third_name']

    # actions = ['mark_as_visible']

    # @admin.action(description='Сделать видимым')
    # def mark_as_visible(self, request, queryset):
    #     queryset.update(is_visible=True)


@admin.register(Otryad)
class SmenaAdmin(admin.ModelAdmin):
    model = Otryad
    inlines = [
        ProfilePhotoInline
    ]


@admin.register(Smena)
class SmenaAdmin(admin.ModelAdmin):
    model = Smena
    inlines = [
        ProfilePhotoInline
    ]
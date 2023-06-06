from django.contrib import admin
from django.shortcuts import redirect
from .models import *
from .data.export import export_obhchiu_s, export_obhchiu, export_soc, export_uchet_putevok

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
                'fields':["ped_zav_full","state","ped_zav_type"]
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


@admin.register(Otryad)
class SmenaAdmin(admin.ModelAdmin):
    model = Otryad
    inlines = [
        ProfilePhotoInline
    ]

    actions = ["export_obhchiu_s"]
    @admin.action(description="Экспорт общей таблицы")
    def export_obhchiu(modeladmin, request, queryset):
        
        for query in queryset:
            print("="*32)
            print(query)
            print(query.__dir__())

            path = export_obhchiu_s(query)

        return redirect("/media/" + path)


@admin.register(Smena)
class SmenaAdmin(admin.ModelAdmin):
    model = Smena
    inlines = [
        ProfilePhotoInline
    ]

    actions = ["export_obhchiu","export_soc_har","export_uchet_putevok"]

    @admin.action(description="Экспорт общей таблицы смены")
    def export_obhchiu(modeladmin, request, queryset):
        
        for query in queryset:
            print("="*32)
            print(query)
            print(query.__dir__())

            path = export_obhchiu(query)

        return redirect("/media/" + path)
    
    @admin.action(description="Экспорт соц характеристики")
    def export_soc_har(modeladmin, request, queryset):
        
        for query in queryset:
            print("="*32)
            print(query)
            print(query.__dir__())

            path = export_soc(query)

        return redirect("/media/" + path)
    
    @admin.action(description="Эскспорт учета путевок")
    def export_uchet_putevok(modeladmin, request, queryset):
        
        for query in queryset:
            print("="*32)
            print(query)
            print(query.__dir__())

            path = export_uchet_putevok(query)

        return redirect("/media/" + path)
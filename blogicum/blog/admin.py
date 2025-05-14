<<<<<<< HEAD


# Register your models here.
=======
# blog/admin.py

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Category, Location, Post

# Классы ModelAdmin для каждой модели
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'slug')
        }),
        (_('Публикация'), {
            'fields': ('is_published', 'created_at'),
            'description': _('Настройки публикации категории')
        }),
    )

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Публикация'), {
            'fields': ('is_published', 'created_at'),
            'description': _('Настройки публикации местоположения')
        }),
    )

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published', 'pub_date')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'

    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'author', 'category', 'location')
        }),
        (_('Публикация'), {
            'fields': ('is_published', 'pub_date', 'created_at'),
            'description': _('Настройки публикации записи')
        }),
    )

# Явная регистрация моделей
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)

# Перевод названия приложения
admin.site.site_header = _('Администрирование Блога')
admin.site.index_title = _('Панель управления блогом')
>>>>>>> 9b093877e7dfd446599721c22d85fee1f4ec66e2

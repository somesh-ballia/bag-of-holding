from django.contrib import admin

from . import models


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['__str__', 'actor', 'verb', 'action', 'preposition', 'target', 'public', 'created']
    list_filter = ['public', 'created']
    readonly_fields = ['created', 'modified']
    search_fields = ['verb']
admin.site.register(models.Event, EventAdmin)


class FollowAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['__str__', 'user', 'actor', 'created']
    list_filter = ['created']
    readonly_fields = ['created', 'modified']
admin.site.register(models.Follow, FollowAdmin)

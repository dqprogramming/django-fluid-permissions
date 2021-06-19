from django.contrib import admin

from fluid_permissions import models


class ViewGroupAdmin(admin.ModelAdmin):
    list_display = ('view_name',)
    filter_horizontal = ('groups',)


admin_list = [
    (models.ViewGroup, ViewGroupAdmin),
]

[admin.site.register(*t) for t in admin_list]

from django.contrib import admin

from scavenger_hunt import models


class ScavengerHuntAdmin(admin.ModelAdmin):
    """
    Admin for the Scavenger Hunt model.
    """
    fields = ('user', 'title', 'final_text')
    list_display = ('user', 'title')
    search_fields = ('title', 'user')


admin.site.register(models.ScavengerHunt, ScavengerHuntAdmin)

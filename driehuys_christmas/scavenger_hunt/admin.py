from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin

from scavenger_hunt import models


class PuzzleAdmin(SortableAdminMixin, admin.ModelAdmin):
    """
    Admin for the Puzzle model.
    """
    fields = ('hunt', 'title', 'text', 'answer', 'completed',)
    list_display = ('title', 'hunt', 'completed')
    search_fields = ('hunt', 'title', 'text', 'answer')


class ScavengerHuntAdmin(admin.ModelAdmin):
    """
    Admin for the Scavenger Hunt model.
    """
    fields = ('user', 'title', 'final_text')
    list_display = ('user', 'title')
    search_fields = ('title', 'user')


admin.site.register(models.Puzzle, PuzzleAdmin)
admin.site.register(models.ScavengerHunt, ScavengerHuntAdmin)

from django.contrib import admin
import core.models
import accounts.models


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'director')


admin.site.register(core.models.Genre)
admin.site.register(core.models.Movie, MoviesAdmin)
admin.site.register(core.models.Director, DirectorAdmin)

admin.site.register(accounts.models.Profile)

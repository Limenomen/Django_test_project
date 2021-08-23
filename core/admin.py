from django.contrib import admin
import core.models as models


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'director')


admin.site.register(models.Genre)
admin.site.register(models.Movie, MoviesAdmin)
admin.site.register(models.Director, DirectorAdmin)

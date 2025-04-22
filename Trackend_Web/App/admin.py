from django.contrib import admin

from .models import *

admin.site.site_header = "TrackEnd ADMINISTRATION"
admin.site.site_title = "TrackEnd ADMINISTRATION"
admin.site.index_title = "BIENVENUE DANS L'ADMINISTRATION DE TrackEnd "


class AdminUser(admin.ModelAdmin):
    list_display = ('email', 'nom')
    search_fields = ('email', 'nom')
    ordering = ('-nom',)
    list_filter = ('nom',)
    list_per_page = 10
    list_editable = ('nom',)
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected users have been deleted.")
    delete_selected.short_description = "Delete selected users"
admin.site.register(User, AdminUser)

class AdminFile(admin.ModelAdmin):
    list_display = ('date',)
    search_fields = ('date',)
    ordering = ('-date',)
    list_filter = ('date',)
    list_per_page = 10
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected files have been deleted.")
    delete_selected.short_description = "Delete selected files"    

admin.site.register(File, AdminFile)
class AdminPossede(admin.ModelAdmin):
    list_display = ('user', 'file', 'date_ajout')
    search_fields = ('user__nom', 'file__id')
    ordering = ('-date_ajout',)
    list_filter = ('user', 'file')
    list_per_page = 10
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected possessions have been deleted.")
    delete_selected.short_description = "Delete selected possessions"
admin.site.register(Possede, AdminPossede)

class AdminTask(admin.ModelAdmin):
    list_display = ('idTask', 'statut', 'intitule', 'date_limite', 'file')
    search_fields = ('intitule',)
    ordering = ('-date_limite',)
    list_filter = ('statut', 'file')
    list_per_page = 10
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected tasks have been deleted.")
    delete_selected.short_description = "Delete selected tasks"
admin.site.register(Task, AdminTask)

class AdminTag(admin.ModelAdmin):
    list_display = ('idTag', 'nom')
    search_fields = ('nom',)
    ordering = ('-nom',)
    list_filter = ('nom',)
    list_per_page = 10
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected tags have been deleted.")
    delete_selected.short_description = "Delete selected tags"
admin.site.register(Tag, AdminTag)


class AdminContenir(admin.ModelAdmin):
    list_display = ('task', 'tag')
    search_fields = ('task__intitule', 'tag__nom')
    ordering = ('-task',)
    list_filter = ('task', 'tag')
    list_per_page = 10
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Selected tag-task relationships have been deleted.")
    delete_selected.short_description = "Delete selected tag-task relationships"
# Register your models here.

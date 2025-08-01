from django.contrib import admin
from .models import Person, Skill, Project, Blog, ClientService

# Register Person model
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'number', 'skill')
    search_fields = ('full_name', 'email', 'skill')
    list_filter = ('skill',)
    ordering = ('full_name',)
    fields = ('full_name', 'email', 'address', 'number', 'skill', 'image')
    readonly_fields = ('image',)  # Optional: Make image read-only in edit view

# Register Skill model
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)
    list_filter = ('proficiency',)
    ordering = ('name',)
    fields = ('name', 'proficiency', 'image')

# Register Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_preview')
    search_fields = ('name', 'description')
    ordering = ('name',)
    fields = ('name', 'description', 'file', 'image_file')

    def description_preview(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_preview.short_description = 'Description'

# Register Blog model
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'has_image', 'has_video')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    fields = ('title', 'content', 'image', 'video')

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Image'

    def has_video(self, obj):
        return bool(obj.video)
    has_video.boolean = True
    has_video.short_description = 'Video'

# Register ClientService model
@admin.register(ClientService)
class ClientServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_preview')
    search_fields = ('name', 'description')
    ordering = ('name',)
    fields = ('name', 'description', 'image')

    def description_preview(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_preview.short_description = 'Description'

# Register your models here.


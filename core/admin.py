from django.contrib import admin
from .models import Post


def make_valid(modeladmin,request, queryset):
    queryset.update(valid=True)
make_valid.short_description = "Make selected posts as valid"

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ['title','valid','combine_title_and_valid']
    list_display_links = ['title','combine_title_and_valid']
    list_editable = ['valid']
    list_filter = ['valid']
    search_fields = ['title']
    actions = [make_valid]
    pass

    def combine_title_and_valid(self, obj):
        return f"{obj.title}- {obj.valid}"
from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment
from .models import Member
from django_summernote.admin import SummernoteModelAdmin
@admin.register(Post)

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
#admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Member)
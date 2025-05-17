from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Events, Posts, PostsUsers, PostsComments

admin.site.register(PostsUsers)

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in Events._meta.fields]
    readonly_fields.remove('claim_url')
    readonly_fields.remove('post_url')
    # Add the custom clickable methods
    readonly_fields += ['clickable_claim_url', 'clickable_post_url']
    fields = readonly_fields
    #def claim_url(self, obj):
    #    return format_html('<a href="{}" target="_blank">{}</a>', obj.claim_url, obj.claim_url)
    def clickable_claim_url(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.claim_url, obj.claim_url)
    clickable_claim_url.short_description = "Claim URL"

    def clickable_post_url(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.post_url, obj.post_url)
    clickable_post_url.short_description = "Post URL"

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        readonly = [field.name for field in Posts._meta.fields]

        if request.user.username == 'annotator1':
            readonly.remove('annotator1') 
        elif  request.user.username == 'annotator2':
            readonly.remove('annotator2') 
        else:
            readonly.remove('annotator3') 

        return readonly
    
    list_display = ('title','student_label','annotator1','annotator2','annotator3')

@admin.register(PostsComments)
class PostsCommentsAdmin(admin.ModelAdmin):
    list_filter = ['post_id']
    list_display = ('text', 'post_id')
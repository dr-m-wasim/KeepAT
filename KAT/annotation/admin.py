from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

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
    
    fields = [field.name for field in Posts._meta.fields]
    fields.remove('post_url')
    
    readonly_fields = ['clickable_post_url', 'post_event', 'post_event_label', 'clickable_post_user']
    fields += ['clickable_post_url', 'post_event', 'post_event_label', 'clickable_post_user']  # Add it at the end of the list
    
    def post_event(self, obj):
        event = Events.objects.filter(event_id=obj.event_id).first()
        return event.claim if event.claim else "No Event"
    post_event.short_description = "Event Claim"
    
    def post_event_label(self, obj):
        event = Events.objects.filter(event_id=obj.event_id).first()
        return 'Real' if event.label == '0' else 'Fake'
    post_event_label.short_description = "Event Claim Label"
    
    def clickable_post_url(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.post_url, obj.post_url)
    clickable_post_url.short_description = "Post URL"
    
    def clickable_post_user(self, obj):
        url = reverse('admin:annotation_postsusers_change', args=[obj.pk])
        return format_html('<a href="{}" target="_blank">Change</a>', url)
    clickable_post_user.short_description = "User Information"
    
    def get_readonly_fields(self, request, obj=None):
        readonly = [field.name for field in Posts._meta.fields]
        
        readonly.remove('title')
        
        if request.user.username == 'annotator1':
            readonly.remove('annotator1') 
        elif  request.user.username == 'annotator2':
            readonly.remove('annotator2') 
        else:
            readonly.remove('annotator3') 

        readonly += ['clickable_post_url', 'post_event', 'post_event_label', 'clickable_post_user']
        
        return readonly
    
    list_display = ('title','student_label','annotator1','annotator2','annotator3')
    
@admin.register(PostsComments)
class PostsCommentsAdmin(admin.ModelAdmin):
    list_filter = ['post_id']
    list_display = ( 'text', 'student_label','annotator1','annotator2','annotator3', 'post_id')
    fields = [field.name for field in PostsComments._meta.fields]
    fields += ['post_final_label']
     
    def post_final_label(self, obj):
        post = Posts.objects.filter(post_id=obj.post_id).first()
        import statistics
        final_label = statistics.mode([int(post.annotator1), int(post.annotator2), int(post.annotator3)])
        return 'Real' if final_label == 0 else 'Fake'
    post_final_label.short_description = "Post's Final Label"
    
    def get_readonly_fields(self, request, obj=None):
        readonly = [field.name for field in PostsComments._meta.fields if field.name != request.user.username]
        readonly += ['post_final_label']
        
        return readonly
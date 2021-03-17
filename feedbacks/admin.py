from django.contrib import admin
from feedbacks.models import Feedback
 
 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    list_filter = ('date',)
    search_fields = ('message',)
 
    class Meta:
        model = Feedback
 
 
admin.site.register(Feedback, FeedbackAdmin)
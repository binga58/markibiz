from django.contrib import admin
from .models import User,Event, Feedback,Team
from .forms import FeedbackForm


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ["name","email","message"]
    form = FeedbackForm


class TeamAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ["name","email","level"]


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["name","email_id"]


admin.site.register(User,UserAdmin)
admin.site.register(Event)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Team,TeamAdmin)

# Register your models here.

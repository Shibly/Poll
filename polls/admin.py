__author__ = 'shibly'

from django.contrib import admin
from polls.models import Choice, Poll
# admin.site.register(Poll)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [('Question Name', {'fields': ['question']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]

    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['questions']
    date_hierarchy = 'pub_date'

# Need to follow the pattern. Create a Model Admin object first
# here PollAdmin is the Model Admin and pass it as the second argument as the admin.site.register()
# If want to change the admin option for an object.
admin.site.register(Poll, PollAdmin)

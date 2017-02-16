from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from .models import *

admin.site.register(Areas)
admin.site.register(Speakers)
admin.site.register(ImportantDates)
admin.site.register(TopicAreas)

admin.site.register(Footer)
admin.site.register(Organizers)
admin.site.register(Publications)


class BaseInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event_type', 'event_title', 'event_date', 'event_place', 'language']}),
        ('Submission', {'fields': ['submission_open', 'submission_details', 'submission_help']}),
        ('Works invitation', {'fields': ['works_invitation']})
    ]


class SubmissionResource(resources.ModelResource):
    class Meta:
        model = Submission
        exclude = ('id',)
        widgets = {
            'created_at': {'format': '%d.%m.%Y'},
        }

class SubmissionAdmin(ImportExportModelAdmin):
    list_display = ('submission_info','title', 'first_name', 'second_name',
                    'company', 'job_position', 'attendance_status',
                    'section_1', 'email', 'telephone')
    list_filter = ['title', 'attendance_status', 'section_1', 'section_2', 'get_review', 'accompanying', 'visa', 'hotel']
    search_fields = ['first_name', 'second_name', 'company', 'job_position', 'abstract_title',
                     'abstract_text', 'email', 'telephone', 'citizenship', 'passport', 'city', 'postal_address',
                     'country']
    list_display_links = (['submission_info'])
    resource_class = SubmissionResource

    def submission_info(self, obj):
        return "Full info"
    submission_info.short_description = 'Info'


admin.site.register(Submission, SubmissionAdmin)
admin.site.register(BaseInfo, BaseInfoAdmin)



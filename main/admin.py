from django.contrib import admin
from main.models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=("name", "date_created", "time_created")
admin.site.register(Course, CourseAdmin)



class ClassScheduleAdmin(admin.ModelAdmin):
    list_display=("title", "organizer", "start_date_and_time", "end_date_and_time")
admin.site.register(ClassSchedule, ClassScheduleAdmin)

class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display=("class_schedule", "attendee", "is_present")
admin.site.register(ClassAttendance, ClassAttendanceAdmin)

class QueryAdmin(admin.ModelAdmin):
    list_display=("title", "description", "submitted_by", "assigned_to", "resolution_status", "date_created")
admin.site.register(Query, QueryAdmin)

class QueryCommentAdmin(admin.ModelAdmin):
    list_display=("query", "comment", "author", "date_created")
admin.site.register(QueryComment, QueryCommentAdmin)



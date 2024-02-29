from django.db import models


from users.models import Cohort, IMUser



class Course(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(default='N/A', blank= True ,null= True)
    date_created= models.DateField(auto_now_add= True, blank = True, null= True)
    time_created = models.DateTimeField(auto_now= True, blank =True, null= True)

    def _str_(self):
        return f"{self.name}"


    
class ClassSchedule(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    start_date_and_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date_and_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_repeated = models.BooleanField (default=True)
    repeat_frequency = models.IntegerChoices
    is_active = models.BooleanField (default=True)
    organizer = models.CharField(max_length=100)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='classes')
    venue = models.CharField(max_length=100)
    facilitator=models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='classes')
    organizer=models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    Course=models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified=models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        start_date_str = self.start_date_and_time.strftime("%d/%m/%Y, %H:%M")
        end_date_str = self.end_date_and_time.strftime("%H:%M")
        return f"{self.title}, {start_date_str} - {end_date_str}"

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name="class_schedule")
    attendee = models.ForeignKey(IMUser,on_delete=models.CASCADE, related_name="class_attendee")
    is_present= models.BooleanField(default=True)
    date_created= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified= models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name="class_author")

    def __str__(self) -> str:
        return f"{self.attendee} - {self.class_schedule}"

class Query(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    submitted_by = models.ForeignKey( IMUser,on_delete=models.CASCADE, related_name="submitted_by")
    assigned_to = models.ForeignKey( IMUser,on_delete=models.CASCADE, related_name="assigned_to")
    resolution_status = models.CharField(
        max_length = 100,
        choices = {
            "PENDING": "PENDING",
            "IN_PROGRESS": "IN PROGRESS",
            "DECLINED": "DECLINED",
            "RESOLVED": "RESOLVED",
        },
        default = 'PENDING'
           )
    
    MEETING_TYPES=(
        ('CLASS_SESSION', 'class_sessions'),
        ('WELLNESS_SESSION', 'well session'),
        ('GUEST_LECTURE', 'Guest Lecture')
    )

 
    date_created= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified= models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name="query_author")

    def __str__(self) -> str:
        return f"{self.title}, {self.author}"


class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete= models.CASCADE, related_name="query_comment")
    comment= models.CharField(max_length=500)
    date_created= models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified= models.DateTimeField(auto_now=True, blank=True, null=True)
    author=models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name="comment_author")

    def _str_(self) -> str:
        return f"{self.comment}, {self.author}"
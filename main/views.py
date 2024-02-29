from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

from users.models import IMUser
from .models import Course
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *
from main.serializers import *
from datetime import *


# Create your views here.
def create_course():
    course = Course.objects.create(name='Science')
    course.save()


def all_courses(req):
    all_courses = Course.objects.all()
    return JsonResponse({
       "result": str(all_courses)
    })


def say_hello(req):
    return HttpResponse("<h1> Hello</h1>")

def filter(req):
    return JsonResponse({
        "firstName": "Sarah",
        "LastName": "Ajekwe",
        "Age":25,
        "phone number": "+2335026077422",
        "email": "ajekwesarah@gmail.com"

    })
def filter_queries(req, query_id):
    data ={
        "id": "Kadoon",
        "title": "EIT",
        "description": "A young lady in trousers and top",
        "status": "verified",
        "submitted": "Succesful"   
    }
    return JsonResponse(
            data
        )

class QueryView(View):
    queries =[
        {"id": 1, "title": "Ad has declined Val status"},
        {"id": 2,"title": "Sammy  Agreed to do it"}
    ]
    def get(self, req):
        return JsonResponse({"result": self.queries})
    
    def post (self, req):
        return JsonResponse({"status": "ok"})
    

@api_view(["GET"])
def fetch_cohort(req):
    #retrieve from db all class schedule
    queryset=ClassSchedule.objects.all()

    #Return queryset result as response
    # Transform/serialize the queryset result to json and send as response
    
    serializer= ClassScheduleSerializer(queryset, many=True)


    #Respond to 
    return Response({"data":serializer.data}, status.HTTP_200_OK)
@api_view (["POST"])
def fetch(request):
    title= request.data.get("title")
    description=request.data.get("description")
    start_date_and_time= request.data.get("start_date_and_time")
    end_date_and_time= request.data.get("end_date_and_time")
    Cohort_id= request.data.get("cohort_id")
    venue= request.data.get("venue")
    facilitator= request.data.get("facilitator")
    course_id= request.data.get("course_id")
    meeting_type= request.data.get("meeeting_type")
    
    if not title:
        return Response({"message":"My friend, send me title"}, status.HTTP_200_OK)
    Cohort=None
    facilitator=None
    Course=None


    #validating the existence of records
    try:
        Cohort= Cohort.objects.get(id=Cohort_id)
    except Cohort.DoesNotExist:
        return Response({"Message":"Masari, this cohort does not exist"}, status.HTTP_200_OK)    

    try:
        Cohort= IMUser.objects.get(id=facilitator)
    except Cohort.DoesNotExist:
        return Response({"Message":"Masari, this cohort does not exist"}, status.HTTP_200_OK)    


    try:
        Cohort= IMUser.objects.get(id=course_id)
    except Cohort.DoesNotExist:
        return Response({"Message":"Masari, this cohort does not exist"}, status.HTTP_200_OK)    
 

    try:
        Cohort= IMUser.objects.get(id=course_id)
    except Cohort.DoesNotExist:
        return Response({"Message":"Masari, this cohort does not exist"}, status.HTTP_200_OK)
    
    class_schedule= ClassSchedule.objects.create(
        title=title,
        description=description,
        venue = venue,
        is_repeated=is_repeated,
        repeat_frequency=repeat_frequency,
        facilitator=facilitator,
        Cohort=Cohort,
        course=course,
        organizer=organizer,
    )
    class_schedule.save()
    serializer=ClassScheduleSerializer(class_schedule, many=False)
    return Response({"message": "schedule successfully created", "data": serializer.data},status.HTTP_200_OK)

 













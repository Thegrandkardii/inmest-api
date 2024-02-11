from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


# Create your views here.   


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

    










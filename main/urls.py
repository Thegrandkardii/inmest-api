from django.urls import path
from .views import *



urlpatterns = [
    path('say_hello/', say_hello),
   path('filter/<int:query_id>', filter_queries),
   path('queries/', QueryView.as_view(), name="query-view"),
   path('all_courses/', all_courses, name="all_courses"),
   path("schedules/fetch/", fetch_cohort),
   path('schedules/fetch',fetch),
   

]
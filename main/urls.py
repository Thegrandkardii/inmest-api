from django.urls import path
from.views import *
from django.contrib import admin

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('say_hello/', say_hello),
   path('filter/<int:query_id>', filter_queries),
   path('queries/', QueryView.as_view(), name="query-view")
]
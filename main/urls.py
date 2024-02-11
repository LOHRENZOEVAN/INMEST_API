from django.urls import path 
from .views import * 

urlpatterns = [
    path ("say_hello/", say_hello),
    path ("user_profile/", user_profile), 
    path ("filter_query/<query_id>/", filter_queries),
    path ("queries/",QueryView.as_view(),)
]
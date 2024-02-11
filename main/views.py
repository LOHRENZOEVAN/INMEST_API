from django.shortcuts import render 
from django.http import JsonResponse, HttpResponse 
from django.views import View

# Create your views here.

def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h1>")  
def user_profile(req):
    data = {
        'name': 'John',
        'email': 'lorenzo@gmail.com',
        'phone': '233535254739'
    }
    return JsonResponse(data)

# 1 write a view function called filter queries 
# 1.a the view function should receive query ID through the url 
#1.b return the jsonresponse data with the following 
# data  id , title,description , status , submitted by 
# 1.c the id should be  

# def  filter_queries(req, id):
    return JsonResponse (
    {
        'id': id,
        'title': 'student',
        'description': 'EIT',
        'status': 'inclass',
        'submitted by': 'bright'
    }
    ) 

def filter_queries(req, query_id):
    query = {
        "id": query_id,
        "title": "trouble ",
        "description": "hoowee",
        "status": "declined", 
        "submitted": "loh"
    }
    return JsonResponse(query_id) 

class QueryView(View): 
    queries = [
         {"id": 1, "title":"Adam declined val shots"},
         {"id": 2, "title":"Adam declined val shots"}
    ]
    def get(self, request):
        return JsonResponse({"results":self.queries})
    def post(self,req):
        return JsonResponse({"status": "ok"})
    
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def homepage(request:HttpRequest):
    response={"message":"Hello World"}
    return JsonResponse(data=response)
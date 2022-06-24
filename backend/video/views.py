from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def video_list(request):
    return JsonResponse(data={'status': 'ok'})

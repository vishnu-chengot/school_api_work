from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import TeacherSerializer


# Create your views here.
@api_view(['POST'])
def add_teacher(request):
    try:
        params = request.data
        serialized_data = TeacherSerializer(data = params)
        if serialized_data.is_valid():
            serialized_data.save()
            msg = 'Data added'
        else:
            msg = 'form not valid'
    except:
        msg = 'something went wrong'
    return JsonResponse({'message':msg})
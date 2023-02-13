from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


# Third Party Import
from rest_framework.views import APIView
from rest_framework.response import Response
class TestView(APIView):
    def get(self, request, *arg, **kwargs):
        data = {
                'name': 'john',
                'age': 23
            }
        return JsonResponse(data)   # safe = False# pass the list in safe




# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }
#     return JsonResponse(data)  # pass the list in safe
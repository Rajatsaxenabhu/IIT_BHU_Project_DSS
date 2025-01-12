from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from .models import DistrictData,Weight
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
def demo(request):
  template = loader.get_template('myfirst.html')
  print(settings.BASE_DIR)
  return HttpResponse(template.render())

@api_view(['POST'])
def get_selected_columns(request):
  if request.method == 'POST':
    print("inside the post method")

  return Response(status=status.HTTP_200_OK)

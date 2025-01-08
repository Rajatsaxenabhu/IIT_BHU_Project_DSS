from django.http import HttpResponse
from django.template import loader
from django.conf import settings
def demo(request):
  template = loader.get_template('myfirst.html')
  print(settings.BASE_DIR)
  return HttpResponse(template.render())


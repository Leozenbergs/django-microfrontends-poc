# from django.shortcuts import render
# from django.views.generic import TemplateView
from django.http import HttpResponse
import datetime

# Create your views here.

# Create your views here.

def get_test(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
# class SecondView(TemplateView):
#   template_name = 'react-test.html'

#   def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context['bundle_js'] = 'react-test/bundle.js'
#       return context
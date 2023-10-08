from django.shortcuts import render
from django.views import generic

# Create your views here.
class HOME(generic.TemplateView):
    template_name= 'bases/home.html'

class About(generic.TemplateView):
    template_name='bases/about.html'

class FAQ(generic.TemplateView):
    template_name = 'bases/faq.html'

class Products(generic.TemplateView):
    template_name = 'bases/products.html'

class Services(generic.TemplateView):
    template_name = 'bases/services.html'
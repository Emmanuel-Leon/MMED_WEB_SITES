from django.urls import path
from .views import HOME, About, FAQ, Products, Services

urlpatterns = [
    path('', HOME.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('faq/', FAQ.as_view(), name='faq'),
    path('products/', Products.as_view(), name='products'),
    path('services/', Services.as_view(), name='services'),
]
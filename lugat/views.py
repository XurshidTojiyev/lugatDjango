from django.shortcuts import render,HttpResponse
from .models import Lugat

def index(request):
    query = request.GET.get('search')
    lugats = Lugat.objects.filter(english=query).all()
    return render(request, 'index.html', {'lugats': lugats})
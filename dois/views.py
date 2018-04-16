from django.shortcuts import render
from crossref.restful import Works


# Create your views here.
def index(request):
    return render(request, "dois/index.html")

def get_doi(request):
    works = Works()
    result = works.doi(request.GET.get('doi'))
    return result

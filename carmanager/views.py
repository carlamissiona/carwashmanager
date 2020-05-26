from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def index(request):
    # <view logic>
    return render(request, 'index.html', {})
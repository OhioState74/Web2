from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb
# Create your views here.


def index(request):
    # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    # context = {'bbs': bbs}
    return render(request, 'bboard/index.html', {'bbs': bbs})

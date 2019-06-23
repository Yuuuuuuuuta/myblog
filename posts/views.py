from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello World! このページは投稿のIndexです。")
    return render(request, 'posts/index.html')

# Create your views here.

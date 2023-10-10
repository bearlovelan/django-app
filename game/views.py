from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">my first web!!!</h1>'
    return HttpResponse(line1)
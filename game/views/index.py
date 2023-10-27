from django.shortcuts import render


def index(request):
    data = request.GET
    context = {
        'access': data.get('access', ""),
        'refresh': data.get('refresh', ""),
    }
    return render(request, "multiends/web.html", context)

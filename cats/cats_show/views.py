from django.http import HttpResponse


def index(request):
    return HttpResponse('<pre><h1>asdasd</h1></pre>' )
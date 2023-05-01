from django.http import HttpResponse

def helloworldfunction(request):
    return HttpResponse('hello world')
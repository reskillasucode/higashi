from django.http import HttpResponse

def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>2回目のhelloworld</h1>')
    return returnedobject
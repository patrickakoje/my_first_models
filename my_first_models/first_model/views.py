from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello World, I just created my first web app, its so cool")


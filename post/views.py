from django.shortcuts import HttpResponse, render
from datetime import date


def hello_view(request):
    return HttpResponse("Hello! It's my project ﾐ🎀・◦・ﾐ")


def current_date_view(request):
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    return HttpResponse(f"Today's date: {formatted_date}")


def goodbye_view(request):
    return HttpResponse('Goodbye user! ﾐ🎀・◦・ﾐ')



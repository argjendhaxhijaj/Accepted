from django.shortcuts import render, redirect
from .models import Events
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import submitEvent
from .forms import submitForm

def index(request):
    return render(request, 'accepted/index.html')

def successs(request):
    return render(request, 'accepted/stories.html')

def places(request):
    return render(request, 'accepted/places.html')

def events(request):
    events = Events.objects.all()
    context = {
        'events': events
    }
    return render(request, 'accepted/events.html', context)

# def submit(request):
#     if request.method == "POST":
#         form = submitForm(request.POST)
#         if form.is_valid():
#             submitEvent = form.save(commit=False)
#             submitEvent.date_posted = timezone.now()
#             submitEvent.save()
#             return render(request, 'accepted/submit.html')
#     else:
#         form = submitForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'accepted/submit.html', context)

def submit(request):
    if request.method == 'POST':
        form = submitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted event')
            return redirect('accepted-submit')
    else:
        form = submitForm()
    return render(request, 'accepted/submit.html', {'form': form})

def about(request):
    return render(request, 'accepted/about.html')
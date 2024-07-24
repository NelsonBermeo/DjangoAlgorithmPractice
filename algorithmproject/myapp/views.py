from django.shortcuts import render
from .forms import TextboxForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TextboxForm(request.POST)
        if form.is_valid():
            #Process the form data
            text = form.cleaned_data['text']
            #Do something with the text
            return render(request, 'home.html', {'form': form, 'text': text})
    else:
        form = TextboxForm()
    
    return render(request, "home.html", {'form': form})
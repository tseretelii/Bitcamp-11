from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django import forms

# Create your views here.

class YourFormName(forms.Form):
    noun = forms.CharField()
    verb = forms.CharField()
    adjective = forms.CharField()
    adverb = forms.CharField()

def index(request):
    # template = render_to_string('myapp/index.html')
    # return HttpResponse(template)
    data = {'title': 'Main Page'}
    return render(request, 'myapp/index.html',data)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    if request.method == 'POST':
        return redirect('success')
    return render(request, 'myapp/contact.html')

def success(request):
    return render(request, 'myapp/success.html')


def your_view_function(request):
    if request.method == 'POST':
        form = YourFormName(request.POST)
        if form.is_valid():
            # Do something with the form data
            noun = form.cleaned_data['noun']
            verb = form.cleaned_data['verb']
            adjective = form.cleaned_data['adjective']
            adverb = form.cleaned_data['adverb']
            mad_lib = f'Do You {verb} your {adjective} {noun} {adverb}? That\'s hilarious!'
            # Render the template with the input value
            return render(request, 'myapp/mad_lib.html', {'input_value': mad_lib})
    else:
        form = YourFormName()


    return render(request, 'myapp/mad_lib.html', {'form': form})
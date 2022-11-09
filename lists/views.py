from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '') # the name attribute of an <input> tag 
    }) # render() builds HttpResponse 
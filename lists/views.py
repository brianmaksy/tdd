from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError

from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

# to handle POST requests too. Not as 'RESTful' but allows one view and url for displaying and creating. 
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError: 
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean() # manually run DB sanitisation (check for empty strings for ex)
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error}) # to check for: adding 2nd empty item to existing list. 
    return redirect(list_) # it uses get_absolute_url() of models.Link directly! 

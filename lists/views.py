from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.forms import ExistingListItemForm, ItemForm

from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


# to handle POST requests too. Not as 'RESTful' but allows one view and url for displaying and creating. 
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})
    # list_ = List.objects.get(id=list_id)
    # error = None

    # if request.method == 'POST':
    #     try:
    #         item = Item(text=request.POST['text'], list=list_)
    #         item.full_clean()
    #         item.save()
    #         return redirect(list_)
    #     except ValidationError: 
    #         error = "You can't have an empty list item"
    # form = ItemForm() 

    # return render(request, 'list.html', {'list': list_, 'form': form, 'error': error})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_) # save directly as opposed to Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


    # # cf DB validation 
    # list_ = List.objects.create()
    # item = Item(text=request.POST['text'], list=list_)
    # try:
    #     item.full_clean() # manually run DB sanitisation (check for empty strings for ex)
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error}) # to check for: adding 2nd empty item to existing list. 
    # return redirect(list_) # it uses get_absolute_url() of models.Link directly! 

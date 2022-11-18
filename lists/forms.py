from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):
    '''ModelForms do all sorts of smart stuff, like assigning sensible HTML form input types to different types of field, and applying default validation. '''

    class Meta:
        '''In Meta we specify which model the form is for, and which fields (of the model) we want it to use.'''
        model = Item
        fields = ('text',) # where name="text" is obtained? # the type below needs to match the type of 'text' in models.List (it is indeed a TextField)
        widgets = {
            # type="text" is from this. Quite sure. 
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }
    def save(self, for_list):
        '''The .instance attribute on a form represents the database object that is being modified or created. '''
        self.instance.list = for_list
        return super().save() # forms.models.ModelForm.save()
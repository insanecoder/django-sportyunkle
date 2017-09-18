from django import forms
from .models import *

class PostForm(forms.ModelForm):
    creatorID = forms.ModelChoiceField(to_field_name='id',queryset=User.objects.all(),widget=forms.Select(attrs={'style':'background_color:#F5F8EC'}))
    tags = forms.ModelChoiceField(required=False,to_field_name='id',queryset=Tag.objects.all(),widget=forms.Select(attrs={'style':'background_color:#F5F8EC'}))
    # tags = forms.ModelMultipleChoiceField(
    #     to_field_name='tagName', # set the value to slug field, not pk/id
    #     required=False,
    #     label=('Additional tags'),
    #     help_text=('Separate by comma to add more than once, or select from available tags'),
    #     queryset=Tag.objects.all(),
    #     widget=forms.SelectMultiple(attrs={
    #         'placeholder': ('Additional tags'),
    #         'class': 'ui search fluid dropdown dropdown-add-tags'
    #     })
    # )

    class Meta:
        model = BlogPost
        fields = ( 'tags','creatorID','blogContent','title','seoTitle','seoDescription','imgPath')

    #creatorID= forms.ModelChoiceField(queryset=User.objects.all())
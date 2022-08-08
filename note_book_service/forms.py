from django import forms

class SearchForm(forms):
    search_word = forms.CharField(label='Search')
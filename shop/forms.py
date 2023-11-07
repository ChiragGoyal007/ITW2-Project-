from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={"class":"form-control mr-sm-2", "type":"search", "placeholder":"Search", "aria-label":"Search"}))
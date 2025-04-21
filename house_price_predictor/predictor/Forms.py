from django import forms

class HouseForm(forms.Form):
    bedrooms = forms.IntegerField()
    bathrooms = forms.FloatField()
    sqft_living = forms.IntegerField()
    floors = forms.FloatField()
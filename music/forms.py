# from django import forms
#
# from django.core.exceptions import ValidationError
#
# class CategoryForm(forms.ModelForm):
#     name=forms.CharField(max_length=128,help_text='Enter category')
#     views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     class Meta:
#         model=Category
#         fields='__all__'
#
# class PageForm(forms.ModelForm):
#     title=forms.CharField(max_length=128,help_text="Enter title")
#     url=forms.URLField(max_length=200,help_text="Please enter the url of the page")
#     views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
#     class Meta:
#         model = Page
#     # What fields do we want to include in our form?
#     # This way we don't need every field in the model present.
#     # Some fields may allow NULL values, so we may not want to include them...
#     # Here, we are hiding the foreign key
#         fields=('title','url','likes')
#
# class User(forms.ModelForm):
#     name=forms.CharField(max_length=100,help_text="Enter Username")
#     userid=forms.CharField(max_length=100,help_text="Enter userid")
#     password=forms.CharField(max_length=100,help_text="Enter password")
#     class Meta:
#         model=Users
#         fields=['name','userid','password']
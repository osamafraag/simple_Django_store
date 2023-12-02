

from django import  forms
from categories.models import Category
from django.core.exceptions import ValidationError



class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

# class CategoryForm(forms.Form):
#     name = forms.CharField()
#     description = forms.CharField(required=False)
#     image = forms.ImageField(required=False)


#     def clean_name(self):

#         found = Category.objects.filter(name=self.cleaned_data['name']).exists()
#         if found:
#             raise ValidationError("Category name already exists")
#         return self.cleaned_data['name']



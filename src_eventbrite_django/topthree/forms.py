from django import forms

from .models import Categories


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ["category_1", "category_2", "category_3"]

    def clean_category_1(self):
        category_1 = self.cleaned_data.get("category_1")
        category_2 = self.cleaned_data.get("category_2")
        category_3 = self.cleaned_data.get("category_3")

        if category_1 == category_2 or category_1 == category_3:
            raise forms.ValidationError("Please select three different categories")

        return category_1

    def clean_category_2(self):
        category_1 = self.cleaned_data.get("category_1")
        category_2 = self.cleaned_data.get("category_2")
        category_3 = self.cleaned_data.get("category_3")

        if category_2 == category_1 or category_2 == category_3:
            raise forms.ValidationError("Please select three different categories")

        return category_2

    def clean_category_3(self):
        category_1 = self.cleaned_data.get("category_1")
        category_2 = self.cleaned_data.get("category_2")
        category_3 = self.cleaned_data.get("category_3")

        if category_3 == category_1 or category_3 == category_2:
            raise forms.ValidationError("Please select three different categories")

        return category_3



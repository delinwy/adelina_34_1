from django import forms

from post.models import Product, Category, Review


class ProductCreateForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    product_price = forms.IntegerField(min_value=0, max_value=1000000)

    def clean(self):
        cleaned_data = super().clean()
        product_description = cleaned_data.get('product_description')
        if len(product_description) < 5:
            raise forms.ValidationError('Description is too short!')
        return cleaned_data


class CategoryForm(forms.Form):
    description = forms.CharField(max_length=300)


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

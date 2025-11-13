from django import forms
from .models import Product

class ProductListingForm(forms.ModelForm):
    """Form for sellers to list their handmade products"""
    
    class Meta:
        model = Product
        fields = ['Product_Name', 'Cateogary', 'Price', 'Description', 'image']
        
        labels = {
            'Product_Name': 'Product Name',
            'Cateogary': 'Category',
            'Price': 'Price (₹)',
            'Description': 'Product Description',
            'image': 'Product Image',
        }
        
        widgets = {
            'Product_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name',
                'maxlength': '50'
            }),
            'Cateogary': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[
                ('Web Applications', 'Pottery & Ceramics'),
                ('Graphical Applications', 'Jewelry & Accessories'),
                ('Console Applications', 'Textiles & Fabrics'),
            ]),
            'Price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price in rupees',
                'min': '1'
            }),
            'Description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your handmade product in detail...',
                'rows': 6,
                'maxlength': '1000'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
        
    def clean_Price(self):
        price = self.cleaned_data.get('Price')
        if price and price < 1:
            raise forms.ValidationError('Price must be at least ₹1')
        return price
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check file size (max 5MB)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Image file size must be less than 5MB')
        return image

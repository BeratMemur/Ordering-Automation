from django import forms
from products.models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name","price", "image", "isActive", "categories")
        labels = {
            "name": "Ürün Adı: ",
            "price": "Ürün Fiyatı: ",
            "image": "Ürün Görseli: ",
            "isActive": "Ürün Aktif mi? ",
            "categories": "Ürün Kategorisi: "
        }
        widgets = {
            "name": forms.TextInput(attrs={"class":"form"}),
            "price": forms.TextInput(attrs={"class": "form"}),
            "categories": forms.CheckboxSelectMultiple(attrs={"class":"select-box"})
        }
        error_messages = {
            "name": {
                "required": "Ürünün adını giriniz",
                "max_length": "Ürün adı en fazla 25 karakterden oluşabilir"
            },
            "price": {
                "required": "Ürünün fiyatını giriniz",
            }
        }

class UploadForm(forms.Form):
    image = forms.ImageField(label="Görsel")

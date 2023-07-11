from django import forms

from main.Product.models import Products, Subject

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():  # стилизация (нужно в каждый класс)
            field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Products
        fields = ('id', 'name', 'category', 'image')

    def clean_name(self):
        name = self.cleaned_data["name"]
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError("Название продукта содержит запрещенное слово.")

        return name

class SubjectForm( StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Subject
        fields = "__all__"


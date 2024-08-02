import re
from django import forms

from orders.models import Order


class CreateOrderForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "requires_delivery",
            "delivery_address",
            "payment_on_get",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices = [
            (0, False),
            (1, True)
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices = [
            (0, False),
            (1, True)
        ],
    )

    
    def clean_phone_number(self):
        data: str = self.cleaned_data["phone_number"]

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")

        pattern = re.compile(r'^\d{11}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        
        return data
    


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


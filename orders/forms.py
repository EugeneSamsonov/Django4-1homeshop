from django import forms

from orders.models import Order


class CreateOrderForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = (
            "user",
            "created_timestamp",
            "phone_number",
            "requires_delivery",
            "delivery_address",
            "payment_on_get",
            "is_paid",
            "status"
        )

    user = forms.CharField()
    created_timestamp = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.CharField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.CharField()
    is_paid = forms.CharField()
    status = forms.CharField()


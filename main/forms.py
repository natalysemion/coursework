# forms.py

from django import forms
from .models import Event

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['event', 'artist', 'type', 'price', 'status']
        # Додайте інші поля, які ви хочете включити до форми

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Можливо, ви хочете додати додаткові налаштування для полів форми тут

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'is_complete', 'date_time', 'place', 'price', 'amount']

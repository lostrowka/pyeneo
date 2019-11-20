from django import forms


# Class representing form which user needs to fill. It consists just of the fields
class ItemForm(forms.Form):
    item_name = forms.CharField(label='Nazwa przedmiotu', max_length=240, required=False)
    quantity = forms.IntegerField(label='Liczba sztuk', min_value=1, max_value=99, required=False)
    min_price = forms.IntegerField(label='Cena minimalna', required=False)
    max_price = forms.IntegerField(label='Cena maksymalna', min_value=1, required=False)
    min_reputation = forms.IntegerField(label='Minimalna reputacja sprzedawcy', required=False)

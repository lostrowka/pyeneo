from django import forms


# Class representing form which user needs to fill. It consists just of the fields
class ItemForm(forms.Form):
    item_name = forms.CharField(label='', max_length=240, required=False,
                                widget=forms.TextInput(attrs={
                                    'class': 'input100',
                                    'placeholder': 'Nazwa przedmiotu',
                                    'type': 'text',
                                    ' name': 'name'},
                                ))

    quantity = forms.IntegerField(label='', min_value=1, max_value=99, required=False,
                                  widget=forms.TextInput(attrs={
                                      'class': 'input100',
                                      'placeholder': 'Ilosc',
                                      'type': 'text',
                                      'name': 'name'},
                                  ))

    min_price = forms.IntegerField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'input100',
        'placeholder': 'Cena minimalna',
        'type': 'text',
        ' name': 'name'},
    ))

    max_price = forms.IntegerField(label='', min_value=1, required=False,
                                   widget=forms.TextInput(attrs={
                                       'class': 'input100',
                                       'placeholder': 'Cena maksymalna',
                                       'type': 'text',
                                       ' name': 'name'},
                                   ))

    min_reputation = forms.IntegerField(label='', required=False,
                                        widget=forms.TextInput(attrs={
                                            'class': 'input100',
                                            'placeholder': 'Minimalna reputacja sprzedawcy',
                                            'type': 'text',
                                            ' name': 'name'},
                                        ))

from django.contrib.auth.forms import forms

class Subscribe(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Message = forms.CharField()
    def __str__(self):
        return self.Email

class PersonalDataForm(forms.Form):
   first_name = forms.CharField(required=True, max_length=255)
   last_name = forms.CharField(required=True, max_length=255)
   email = forms.EmailField(required=True)
   phone = forms.CharField(required=True, max_length=200)
   address = forms.CharField(max_length=1000, widget=forms.Textarea())


class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(label = "Do you like this website?", choices = ((1, "Yes"), (0, "No")), coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,initial = '1', required = True,)
    favorite_food = forms.CharField(label = "What is your favorite food?", max_length = 80, required = True, )
    favorite_color = forms.CharField(label = "What is your favorite color?",max_length = 80, required = True,)
    favorite_number = forms.IntegerField(label = "Favorite number",required = False,)
    notes = forms.CharField(label = "Additional notes or feedback",required = False,)

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address1', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}) )
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
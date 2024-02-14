from django import forms

PROBLEMS = (
    ('family', "Family"),
    ('business', "Business"),
    ('relationships', "Relationships"),
    ('other', "Other")
)


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
#    problem = forms.ChoiceField(choices=PROBLEMS, widget=forms.Select(), required=True)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)


class SecondForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)


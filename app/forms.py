from django import forms

from app.models import UserData


class ContactForm(forms.Form):
    first_name = forms.CharField(
        label="Ism",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Sizning ismingiz"}
        ),
    )

    last_name = forms.CharField(
        label="Familiya",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Sizning familiyangiz"}
        ),
    )

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "example@mail.ru"}
        ),
    )

    phone_number = forms.CharField(
        label="Telefon Raqam",
        max_length=15,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+998 (__) ___-__-__"}
        ),
    )

    message = forms.CharField(
        label="Xabar",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Sizning xabaringiz...",
            }
        ),
    )


class PostTableForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["first_name", "last_name", "email", "phone_number", "message"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }

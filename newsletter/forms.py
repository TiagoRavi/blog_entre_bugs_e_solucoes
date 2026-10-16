from django import forms


class SubscriptionForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        label="Seu e-mail",
    )
    consent = forms.BooleanField(
        required=True,
        error_messages={
            "required": "Você precisa autorizar o recebimento da newsletter."
        },
    )

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()
from django import forms


class ParticipantForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        strip=True,
        help_text="use another place if it already exists",
    )
    description = forms.CharField(
        max_length=500,
        strip=True,
        help_text="write some description",
    )
    type = forms.CharField(
        max_length=80,
        strip=True,
        help_text="type of the place - (restaurant, cafe)",
    )
    location = forms.CharField(
        max_length=80,
        strip=True,
        help_text="location of your place",
        required=False,
    )
    rating = forms.IntegerField(min_value=1, max_value=5)

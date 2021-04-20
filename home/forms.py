from django import forms


class Users(forms.Form):
    """User definition."""

    # TODO: Define form fields here
    username = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False,)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)


class Article(forms.Form):
    """article definition."""

    # TODO: Define form fields here
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'title', 'class': 'form-control'}), max_length=255, required=False)
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'content', 'class': 'form-control'}), required=False)
    category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[
                                 ('politik', 'politik'), ('agama', 'agama'), ('education', 'education')], required=False)

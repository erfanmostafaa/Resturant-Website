from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", max_length=100)

class CommentForm(forms.Form):
    body = forms.TextInput()
    score = forms.IntegerField(min_value=1, max_value=5)

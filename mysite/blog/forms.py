from django import forms


class EmailPostForm(forms.Form):
    # 这个会被渲染成<input type="text">
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)

from django import forms
from main.models import Article
from main.validators import validate_title


class Article_form(forms.ModelForm):
    title = forms.CharField(required=True, validators=[validate_title])

    class Meta:
        model = Article
        fields = [
            "title",
            "body",
            "num_slug"
        ]

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if body == "":
            raise forms.ValidationError("!لا يمكن ترك هذا الحقل فارغا")
        return body

    def clean_num_slug(self):
        num_slug = self.cleaned_data.get("num_slug")
        if num_slug < 1 or num_slug > 3:
            raise forms.ValidationError("الرقم {} لا يقابل اي نوع من المقالات".format(num_slug))
        return num_slug

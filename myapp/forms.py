from django import forms
from .models import Contact

SUBJECT_CHOICES = (
    ("I", "Inquiry"),
    ("C", "Complaint")
)

# # FIRST METHOD(REGULAR)
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(label="Your email")
#     subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
#     message = forms.CharField(widget=forms.Textarea)

# SECOND METHOD
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message", "subject"] #OR fields = "__all__"
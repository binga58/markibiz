from django import forms
from .models import Feedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Field,Div
from crispy_forms.bootstrap import PrependedText
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['name','email','message']
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            PrependedText('email', '@', placeholder="username"),
            Fieldset(
            Div(

            css_id = 'specials'
            ),

        ),

        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),
            Field('email',css_class="password-fields"),
            )

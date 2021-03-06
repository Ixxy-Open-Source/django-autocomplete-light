from dal import autocomplete

from django import forms

from .models import TestModel


def get_choice_list():
    return [model.test for model in TestModel.objects.all()]


class TestForm(forms.ModelForm):
    test = autocomplete.Select2ListCreateChoiceField(
        choice_list=get_choice_list,
        required=False,
        widget=autocomplete.ListSelect2(url='select2_list')
    )

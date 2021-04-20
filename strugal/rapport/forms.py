from django import forms
from django.forms import BaseModelFormSet
from django.forms import modelformset_factory
from django.forms import inlineformset_factory
from .models import RapportJournalier
from planing.models import ProductionPlan
import time
from django.db.models import Q


class BaseFormSet(BaseModelFormSet):
    class Meta:
        model = RapportJournalier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # profile = Profile.objects.get(user=kwargs.pop("request").user)
        super(BaseFormSet, self).__init__(*args, **kwargs)

        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%Y-%m-%d", named_tuple)
        # self.queryset = RapportJournalier.objects.all()
        # #   ProductionPlan.objects.filter(
        # #     Q(date_created=time.strftime(
        # #         "%Y-%m-%d", time.localtime()))).values_list('ref', flat=True)
        # print(self.queryset)

        # self.fields['ref'] = forms.ModelChoiceField(
        #     queryset=ProductionPlan.objects.filter(Q(
        #         date_created=time_string)).values_list('ref', flat=True))

        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'form-control'


RapportFormset = inlineformset_factory(
    ProductionPlan,
    RapportJournalier,
    fields=(
        'ref',
        'prod_physique',
        'prod_conforme',
    ),
    formset=BaseFormSet,
)


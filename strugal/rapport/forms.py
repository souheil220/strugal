from django import forms
from .models import RapportJournalier
from planing.models import ProductionPlan
import time
from django.db.models import Q


class RapportForm(forms.ModelForm):
    class Meta:
        model = RapportJournalier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # profile = Profile.objects.get(user=kwargs.pop("request").user)
        super(RapportForm, self).__init__(*args, **kwargs)

        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%Y-%m-%d", named_tuple)

        # print(time_string)

        # test = self.fields['ref'] = RapportJournalier.objects.all()
        # references = []

        # for refer in test:
        #     references.append(refer.ref.ref)
        # print(references)
        self.fields['ref'] = forms.ModelChoiceField(
            queryset=ProductionPlan.objects.filter(Q(
                date_created=time_string)))
        # .exclude(ref__in=references))
        #  ~Q(ref__in=references)
        # test =

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

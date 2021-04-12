from django.shortcuts import render
from .forms import RapportForm


# Create your views here.
def rapport(request):
    formset = RapportForm()
    if request.method == 'POST':
        formset = RapportForm(request.POST)
        if formset.is_valid():
            formset.save()
    return render(request, "rapport/index.html", {
        'formset': formset,
    })

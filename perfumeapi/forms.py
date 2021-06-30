from django.forms import ModelForm
from perfumeapi.models import Perfumes

# Create the form class.

class PerfumesForm(ModelForm):
    class Meta:
        model = Perfumes
        fields = ['nome', 'familiaOlfativa', 'marca', 'volumetria']

# Creating a form to add an article.
# form = PerfumesForm()

# Creating a form to change an existing article.
# Perfumes = Perfumes.objects.get(pk=1)
# form = PerfumesForm(instance=article)
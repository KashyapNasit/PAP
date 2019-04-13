from django.forms import ModelForm
from . models import Batch


class AddBatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_name', 'number_of_groups']
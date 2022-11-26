from django.forms import ModelForm  # this class is used to convert a model into modelform
from .models import MLdata

class UploadForm(ModelForm):
    class Meta: 
        model = MLdata
        fields = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'martial_status', 
        'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hoursperweek', 'native_country']
        exclude = ['prediction']

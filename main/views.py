from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import MLdata
from django.core import serializers
from django.forms.models import model_to_dict
import joblib
import pickle
import sklearn
import pandas as pd
# Create your views here.
def home(request):
    return HttpResponse('ok')

def upload(request):
    if request.POST:
        form = UploadForm(request.POST)
        print(request.POST)
        print('Hi')
        if form.is_valid():
            form.save()
        return redirect(result)
    # When the upload page is called so we will render the upload form html as there is no post data. After filling the form upload function is again called 
    return render(request, 'upload.html', {'form': UploadForm})

def logs(request):
    logs = MLdata.objects.all()
    context = {'logs': logs}
    return render(request, 'logs.html', context)

def result(request):
    filename = 'main/RFmodel.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print('model loaded')
    input_data = MLdata.objects.last()
    data = model_to_dict(input_data)
    print(data)
    data = pd.DataFrame(data, index = [0])
    data = data.drop('prediction', axis=1)

    input_data.prediction = loaded_model.predict(data)
    input_data.save()
    return  render(request, 'result.html', {'input_data': input_data})

def test(request):
    print('enter test')
    filename = 'main/RFmodel.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    print('model loaded')
    print(model)
 







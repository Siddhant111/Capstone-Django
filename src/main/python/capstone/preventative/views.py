from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.

def preventative(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        dataset = pd.read_excel(settings.BASE_DIR + uploaded_file_url)
        dataset = dataset.drop([0])
        dataset = dataset.drop([1])
        dataset = dataset.drop([95])
        dataset = dataset.rename(columns={
            'Type': 'Row Labels',
            'TRUE': 'Count of Doctors',
            'Unnamed: 2': 'Centers',
            'Unnamed: 3': 'Population',
            'Unnamed: 4': 'Areas',
            'Unnamed: 5': 'Zones',
        })
        imputer = Imputer(missing_values = 'nan', strategy = 'mean', axis = 0)
        dataset = dataset.dropna(how='any')
        labelencoder_X = LabelEncoder()
        obj=dataset['Areas'].groupby(dataset['Zones'])
        plt.scatter(dataset['Count of Doctors'], dataset['Zones'])
        plt.show()
        sheets = pd.read_excel(settings.BASE_DIR + uploaded_file_url,sheet_name=['sum'])
        dataset1 = pd.concat(sheets[frame] for frame in sheets.keys())
        dataset1 = dataset1.drop([2])
        dataset1 = dataset1.rename(columns={
            'Unnamed: 0': 'Row Labels',
            'Unnamed: 1': 'Area',
            'Unnamed: 2': 'Count of center',
            'Unnamed: 3': 'doctors',
            'Unnamed: 4': 'pop',
            'Unnamed: 5': 'Pop/center',
            'Unnamed: 6': 'Pop/Dr',
            'Unnamed: 7': 'Dr/cr',
        })
        imputer = Imputer(missing_values = 'nan', strategy = 'mean', axis = 0)
        dataset1 = dataset1.dropna(how='any')
        labelencoder_X = LabelEncoder()
        plt.scatter(dataset1['Count of center'], dataset1['Area'])
        plt.show()
        return render(request, 'preventative.html', {'uploaded_file_url': uploaded_file_url, 'conclusion': 'ujhbkhxhcgjv'})
    return render(request, 'preventative.html')

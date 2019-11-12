from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Create your views here.

def preventative(request):
    return render(request, 'preventative.html')


def preventative_test(request):
    dataset = pd.read_excel('C:/Users/Siddhant/Desktop/bones-master/data/doctors.xlsx')
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


    return render(request, 'preventative.html')



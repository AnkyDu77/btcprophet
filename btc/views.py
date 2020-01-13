from django.shortcuts import render
import pandas as pd

def index(request):
    #Reading data
    raw_data = pd.read_csv('/home/c15980/btc.na4u.ru/app/ensobit/btc/Data/frontend_data.csv')
    data = raw_data.copy()
    #Preparing front-end data
    dates = list(data['Date'])
    close = list(data['Close'])
    prediction = list(data['Prediction'])

    context = {'dates': dates, 'prices': close,
            'prediction':prediction}

    return render(request, 'btc/index.html',context=context)

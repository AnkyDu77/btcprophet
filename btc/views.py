from django.shortcuts import render
import pandas as pd

def index(request):
    #Reading data
    raw_data = pd.read_csv('/app/btc/Data/frontend_data.csv')
    data = raw_data.copy()
    #Preparing front-end data
    dates = list(data['Date'])
    close = list(data['Close'])
    close[-1] = 'NaN'
    close[-2] = 'NaN'
    lower_line = list(data['Lower_line'])
    upper_line = list(data['Upper_line'])
    colored_area = []
    for i,j in zip(lower_line,upper_line):
        inner_lst=[i,j]
        colored_area.append(inner_lst)

    context = {'dates': dates, 'prices': close, 'colored_area': colored_area,
                'lower_line':lower_line,'upper_line':upper_line}

    return render(request, 'btc/index.html',context=context)

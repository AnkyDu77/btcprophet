from django.shortcuts import render
import pandas as pd
import math

def index(request):
    #Reading data /app/btc/Data/frontend_data.csv
    raw_data = pd.read_csv('/Users/aaraybin/Documents/py4e/mygit/btcprophet/btc/Data/frontend_data.csv')
    data = raw_data.copy()
    #Preparing front-end data
    dates = list(data['Date'])
    close = list(data['Close'])
    for item in close: #Changing float-type nan on string-type nan
        if math.isnan(item):
            close[close.index(item)]='NaN'
    lower_line = list(data['Lower_line'])
    upper_line = list(data['Upper_line'])
    colored_area = []
    for i,j in zip(lower_line,upper_line):
        inner_lst=[i,j]
        colored_area.append(inner_lst)

    context = {'dates': dates, 'prices': close, 'colored_area': colored_area,
                'lower_line':lower_line,'upper_line':upper_line}

    return render(request, 'btc/index.html',context=context)

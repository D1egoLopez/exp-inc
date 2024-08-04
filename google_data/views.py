from django.shortcuts import render
from django.http import HttpResponse
from .google_sheets import get_google_sheet

def get_data_from_sheet():
    sheet = get_google_sheet("DB savings")
    data = sheet.get_all_records()
    return data

def printing(request):
    return render(request,'hello.html')

def get_sheets():
    spreadsheet = get_google_sheet("DB savings")
    sheet1 = spreadsheet.worksheet('EXP')
    sheet2 = spreadsheet.worksheet('INC')
    sheets =[sheet1, sheet2]
    return sheets

def summas(request):
    total_summs = [0,1]
    for i in range(2):
        sheet = get_sheets()[i]
        column_data = sheet.col_values(2)
        column_data = column_data[1:]
        column_data_as_ints = [int(value) for value in column_data if value.isdigit()]
        total_summs[i] = sum(column_data_as_ints)
        #total_summs[0] ==> expensas || total_summs[1] ==> incomes
    egresos = total_summs[0]
    ingresos = total_summs[1]
    return render(request, 'hello.html', {'egresos' : egresos, 'ingresos' : ingresos})



def exp(request):
    sheet = get_sheets()[0]
    data = sheet.get_all_records()
    column_data = sheet.col_values(2)
    column_data = column_data[1:]
    column_data_as_ints = [int(value) for value in column_data if value.isdigit()]
    total_summ = sum(column_data_as_ints)
    return render(request, 'home.html', {'data': data,'total_sum' : total_summ})

def inc(request):
    sheet = get_sheets()[1]
    data = sheet.get_all_records()
    column_data = sheet.col_values(2)
    column_data = column_data[1:]
    column_data_as_ints = [int(value) for value in column_data if value.isdigit()]
    total_summ = sum(column_data_as_ints)
    return render(request, 'home.html', {'data': data, 'total_sum' : total_summ})

# Create your views here.



# E:
# cd Projects
# cd Exp$Inc
# cd google_data

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google_sheets import *
from models import meses


def get_sheets():
    spreadsheet = get_google_sheet("DB savings")
    sheet1 = spreadsheet.worksheet('EXP')
    sheet2 = spreadsheet.worksheet('INC')
    sheets =[sheet1, sheet2]
    return sheets

sheets = get_sheets()
expenses_sheet = sheets[0]
income_sheet = sheets[1]
expenses_sheet_values = expenses_sheet.get_all_values()
income_sheet_values = income_sheet.get_all_values()


def sumas_exp_inc():
    total_summs = [0,0]
    for i in range(2):
        sheet = get_sheets()[i]
        column_data = sheet.col_values(2)
        print(column_data)
        column_data = column_data[1:]
        column_data_as_ints = [int(value) for value in column_data if value.isdigit()]
        total_summs[i] = sum(column_data_as_ints)
        print(total_summs)


def get_last_rows(sheet:list):
    last_row = sheet[-1]
    last_row2 = sheet[-2]
    return [last_row, last_row2]

temp = get_last_rows(expenses_sheet_values)
temp2 = temp[1][1]
print(temp2)
#todo check dates from last 2 rows and if same add ammount al monto de ese mes
print('dada')

def get_last_two_dates(sheet):
    column_data = sheet.col_values(1)
    fecha = column_data[-1]
    fecha_anterior = column_data[-2]
    dia = fecha[:-8]
    dia_anterior = fecha_anterior[:-8]
    mes = fecha[3:5]
    mes_anterior = fecha_anterior[3:5]
    anio_anterior = fecha_anterior[6:]
    anio = fecha[6:]
    return fecha, dia, mes, anio, fecha_anterior, dia_anterior, mes_anterior, anio_anterior

def meses_check(month_str:str):
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    return months.get(month_str, "Invalid month number")

def date_creator():
    return

Year_2024 = {
    "January"
    "February"
    "March"
    "April"
    "May"
    "June"
    "July"
    "August"
    "September"
    "October"
    "November"
    "December"
}


last_entry_date = get_last_two_dates(expenses_sheet)
current_month = last_entry_date[2]
last_month = last_entry_date[6]
current_year = last_entry_date[3]
last_year = last_entry_date[7]
print(current_month, current_year, last_month, last_year)
print("Last two dates: ", last_entry_date)
current_month_exp = 0
sumas_exp_inc()
if current_month == last_month:
    current_month_exp =+ 2

print(meses_check(get_last_two_dates(expenses_sheet)[2]))

    



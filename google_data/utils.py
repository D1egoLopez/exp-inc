# E:
# cd Projects
# cd Exp$Inc
# cd google_data

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google_sheets import *


def get_sheets():
    spreadsheet = get_google_sheet("DB savings")
    sheet1 = spreadsheet.worksheet('EXP')
    sheet2 = spreadsheet.worksheet('INC')
    sheets =[sheet1, sheet2]
    return sheets

def sumas_exp_inc():
    total_summs = [0,0]
    for i in range(2):
        sheet = get_sheets()[i]
        column_data = sheet.col_values(2)
        column_data = column_data[1:]
        column_data_as_ints = [int(value) for value in column_data if value.isdigit()]
        total_summs[i] = sum(column_data_as_ints)
        print(total_summs)

    



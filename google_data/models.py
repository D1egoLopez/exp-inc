from django.db import models

# Create your models here.

class meses():
    def __init__(self, nombre_mes: str, anio: int, income_de_mes: int, expenses_de_mes: int):
        self.nombre_mes = nombre_mes
        self.anio = anio
        self.income_de_mes = income_de_mes
        self.expenses_de_mes = expenses_de_mes
    def __repr__(self):
        return f"Meses(nombre_mes={self.nombre_mes}, anio={self.anio}, income_de_mes={self.income_de_mes}, expenses_de_mes={self.expenses_de_mes})"

#Yunior Dennis
#Fechas en python

from datetime import date, time, datetime

#Fecha actual
hoy = date.today()
print(hoy)

#formatear fecha 
formateado = hoy.strftime("%d/%m/%y")
print(formateado)

#Hora actual
fecha_actual = datetime.now()
print(fecha_actual)

#capturar el año
anio = fecha_actual.year
print(anio)

mes = fecha_actual.month
print(mes)

dia = fecha_actual.day
print(dia)

hora_actual = fecha_actual.strftime("%H:%M:%S")
print(hora_actual)

# Formato AM PM
fecha_am_pm = fecha_actual.strftime("%I:%M:%S %p")
print(fecha_am_pm)



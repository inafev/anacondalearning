Código de ejemplo para procesar datos Excel/CSV
1) Desde un documento Excel creamos el siguiente fichero CSV de ejemplo: Workbook1.csv

Date,Revenue,Cost
3-May-10,1289.41,899.54
4-May-10,951.89,772.12

2) Código de ejemplo csv_reader.py (cuidado con la identación, no se ha mantenido aquí)

import csv
import sys
from optparse import OptionParser

def calculate_profit(day):
return float(day['Revenue']) - float(day['Cost'])

if __name__ == '__main__':
parser = OptionParser()
parser.add_option('-f', '--file', help="CSV Data File")
opts, args = parser.parse_args()

if not opts.file:
parser.error('File name is required')

# Create a dict reader from an open file
# handle and iterate through rows.
reader = csv.DictReader(open(opts.file, 'rU'))
for day in reader:
print '%10s: %10.2f' % \
(day['Date'], calculate_profit(day))

3) Ejecucíón:	
(text_processing)$ python csv_reader.py --file=./Workbook1.csv 

4) Explicación: 
Abrimos el fichero con soporte para Universal Newline para que sea independiente de nuestra plataforma. 
Accedemos a los datos CSV creando una instancia de csv.DictReader seguido de un método csv.reader. Esto requiere acceder cada fila con un índice de array.
La clase DictReader usa por defecto la primera fila en el fichero CSV como un diccionario de claves. Esto simplifica mucho el acceso a los datos por nombre.

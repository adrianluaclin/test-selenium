import csv
from io import StringIO
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def escribir_csv_en_memoria(resultados, cabeceras, delimitador=','):
    memoria = StringIO()
    escritor = csv.writer(memoria, delimiter=delimitador)
    
    escritor.writerow(cabeceras)
    
    for fila in resultados:
        escritor.writerow(fila)
    
    datos_csv = memoria.getvalue()
    memoria.close()
    
    return datos_csv



# Crear el objeto MIMEMultipart para el correo
mensaje = MIMEMultipart()
mensaje['From'] = ''
mensaje['To'] = ''
mensaje['Subject'] = ''

# Adjuntar el archivo CSV 1 al correo

csv_en_memoria_1 = escribir_csv_en_memoria('', '')
adjunto_1 = MIMEText(csv_en_memoria_1, 'csv')
adjunto_1.add_header('Content-Disposition', 'attachment', filename='nombre')
mensaje.attach(adjunto_1)

# Adjuntar el archivo CSV 2 al correo
csv_en_memoria_2 = escribir_csv_en_memoria('','')
adjunto_2 = MIMEText(csv_en_memoria_2, 'csv')
adjunto_2.add_header('Content-Disposition', 'attachment', filename='nombre')
mensaje.attach(adjunto_2)

# Establecer el cuerpo del mensaje
mensaje.attach(MIMEText('', 'plain'))







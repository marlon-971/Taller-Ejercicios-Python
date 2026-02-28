# cargar datos
import pandas as pd
import codecs 
datos = pd.read_csv('data/personas.csv')

texto_original = "JUAN"

# Cifrar (ROT13)
texto_cifrado = codecs.encode(texto_original,'rot_13')
print(f"Cifrado: {texto_cifrado}")

# JUAN = WHNA
condicion = datos['nombre_cifrado']=='Whna'
datos_nuevos = datos[condicion]
print(datos_nuevos)
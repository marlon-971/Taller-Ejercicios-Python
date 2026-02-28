# cargar datos
import pandas as pd
import codecs 
datos = pd.read_csv('data/personas.csv')

texto_original = "MARIA"

# Cifrar (ROT13)
texto_cifrado = codecs.encode(texto_original,'rot_13')
print(f"Cifrado: {texto_cifrado}")

# Marlon = ZNEYBA
condicion = datos['nombre_cifrado']=='Znevn'
datos_nuevos = datos[condicion]
print(datos_nuevos)
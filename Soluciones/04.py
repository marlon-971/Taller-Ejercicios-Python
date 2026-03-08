import pandas as pd
import codecs

df = pd.read_csv('data/personas.csv')

df['nombre'] = df['nombre_cifrado'].apply(
    lambda x: codecs.decode(str(x), 'rot_13').strip().title()
)

conteo = df['nombre'].value_counts()

# idxmax() → devuelve el valor más frecuente
# max() → cantidad
print(conteo.idxmax(), conteo.max())

# Proyecto De Titulacion 2017 NV-DC-UPIIC

El siguiente es un proyecto de Titulacion de la Unidad Profecional Interdiciplinaria de Ing. Ciencias Sociales y Administrativas 2017.
Desarrollado por MML2oi56oi2f9
## Lista de requerimientos

- El sofware debe ser rentable, factible y funcional.
- Facil de usar 
- Analizar los datos de la manera mas rapida posible
- Velocidad de procesamiento y analisis
- Portable
- Corta periodo de aprendizaje
- Tiene que funcionar en computadoras de baja gama
- Detectar Patrones determinadas
- Descartar muestras erroneas
- Descartar erroes
- Analizar nuevos patrones
- Reconoces patrones repetitivos
- Exportar los resultados en un archivo de excel
- Presentacion sencilla de los datos
- Procesar la imagen para su manipulacion

## Modelos

#### Diagramas de procesos

#### Diagramas de Caso de Uso

#### Diagramas de clase

#### Diagrama Relacional

## Code

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
```
Importamos las librerias.

```
fp = Image.open('neu.jpg')
iar = np.asarray(fp)
plt.imshow(iar)
print (iar)
plt.show()
```
```python
#!/usr/bin/env python
import random

## Datos de hombres y mujeres
input_data = [[170,56,1], # Mujer de 1.70m y 56kg
              [172,63,0],# Hombre de 1.72m y 63kg
              [160,50,1], # Mujer de 1.60m y 50kg
              [170,63,0], # Hombre de 1.70m y 63kg
              [174,66,0],# Hombre de 1.74m y 66kg
              [158,55,1],# Mujer de 1.58m y 55kg
              [183,80,0],# Hombre de 1.83m y 80kg
              [182,70,0],# Hombre de 1.82m y 70kg
              [165,54,1]]# Mujer de 1.65m y 54kg

## Creamos el perceptron

weights = [] # Lista con los pesos
errors = []  # Lista con los errores


class Perceptron:
    def __init__(self,input_number,step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size
        
    def predict(self,inputs):
        weighted_average = sum(w*elm for w,elm in zip(self._w,inputs))
        if weighted_average > 0:
            return 1
        return 0

    def train(self,inputs,ex_output):
        output = self.predict(inputs)
        error = ex_output - output
        if error != 0:
            self._w = [w+self._eta*error*x for w,x in zip(self._w,inputs)]
        return error
      
pr = Perceptron(3,0.1) # Perceptron con 3 entradas
## Fase de entrenamiento
for _ in range(100):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
      height, weight, gender = person
      # Agregamos un uno por default
      inp = [1, height, weight]
      weights.append(pr._w)
      errors.append(pr.train(inp, gender))

h = float(input("Introduce tu estatura en centimetros.- "))
w = float(input("Introduce tu peso en kilogramos.- "))

if pr.predict([1,h,w]) == 1: print ("Mujer")
else: print ("Hombre")

#print """
#Nota: El resultado puede estar incorrecto. 
#Esto puede ser debido a sesgo en la muestra, o porque es imposible separar
#a hombres y mujeres perfectamente basados unicamente en talla y peso."""

## Fase de graficacion
import imp

can_plot = True
try:
    imp.find_module('matplotlib')
except:
    can_plot = False

if not can_plot:
    print ("No es posible graficar los resultados porque no tienes matplotlib")
    sys.exit(0)
    pass

import matplotlib.pyplot as plt

plt.plot(errors)
plt.show()
```


Invocamos la imagen del metodo Image.

## Bibliografia

### Farmacologia

http://www.redalyc.org/pdf/579/57932293004.pdf

https://digitalis-dsp.uc.pt/bitstream/10316.2/36774/1/La%20Farmacología%20Nacional.pdf

http://www.cuc.udg.mx/sites/default/files/publicaciones/2015%20-%20Manual%20de%20conocimientos%20básicos%20de%20farmacología.pdf

http://bibmed.ucla.edu.ve/edocs_bmucla/materialdidactico/farmacologia/farmbasica.pdf

http://www.uaa.edu.mx/libros/FARMACOLOGIA%20Y%20NUTRICI%E0N/FARMACOLOG%D6A%201..pdf

### Requerimientos & Diseño

http://www.info.univ-angers.fr/pub/maturana/files/Modelamiento_de_Software_y_Negocios.pdf

http://www.inf-cr.uclm.es/www/mpolo/asig/0708/manualPrincipal.pdf

### Reconocimiento de Patrones

[Hammels](http://www.cs.ukzn.ac.za/~sviriri/Books/Machine-Learning-Pattern-Recognition/book1.pdf)

http://www.cs.ukzn.ac.za/~sviriri/Books/Machine-Learning-Pattern-Recognition/book2.pdf

http://www.cs.ukzn.ac.za/~sviriri/Books/Machine-Learning-Pattern-Recognition/book3.pdf

http://www.cs.ukzn.ac.za/~sviriri/Books/Machine-Learning-Pattern-Recognition/book4.pdf

http://www.cs.ukzn.ac.za/~sviriri/Books/Machine-Learning-Pattern-Recognition/book5.pdf

http://www.cs.ukzn.ac.za/~sviriri/Books/Machine-Learning-Pattern-Recognition/book6.pdf

### Vision Artificial

http://www.etitudela.com/celula/downloads/visionartificial.pdf

http://eprints.ucm.es/11587/1/Tutorial-IA-Programacion.pdf

http://www.it.uc3m.es/jvillena/irc/practicas/estudios/Emocion.pdf

http://ri.uaemex.mx/bitstream/handle/20.500.11799/63881/secme-35486.pdf?sequence=1

## WebBiografia
https://www.google.com.mx/search?ei=X80VWqjWAae7jwSZx60Y&q=image+counter+python&oq=image+counter+python&gs_l=psy-ab.3...12031.12931.0.13467.5.5.0.0.0.0.205.399.0j1j1.2.0....0...1c.1.64.psy-ab..3.0.0....0.hdnNRSd_aOQ

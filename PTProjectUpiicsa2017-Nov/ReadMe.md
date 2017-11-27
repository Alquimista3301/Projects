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

fp = Image.open('neu.jpg')
iar = np.asarray(fp)
plt.imshow(iar)
print (iar)
plt.show()
```
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

http://www.cs.ukzn.ac.za/~sviriri/Books/Machine-Learning-Pattern-Recognition/book1.pdf

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

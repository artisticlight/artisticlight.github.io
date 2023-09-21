# Búsqueda

Cada función de búsqueda devuelve un objeto ''ASFSearchResults'':

- '''geo_search()''' Buscar información del producto en un área de interés usando una cadena WKT
- '''granule_search()''' Buscar información del producto usando una lista de nombres de escenas
- '''product_search()''' Buscar información del producto utilizando una lista de ID de producto
- '''stack_from_id()''' Buscar una pila de línea base de productos utilizando un ID de escena de referencia
- Si los enfoques de búsqueda anteriores no satisfacen sus necesidades de búsqueda, ''search()''' admite todas las palabras clave disponibles:
    - '''search()''' Encuentre información del producto utilizando cualquier combinación de parámetros de búsqueda. Vea la lista de palabras clave a continuación.

Se pueden encontrar ejemplos de algunos flujos de trabajo de búsqueda en este [script de ejemplo](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/hello_world.py). También puede hacer referencia a [Jupyter notebooks](https://github.com/asfadmin/Discovery-asf_search/tree/master/examples) por ejemplo flujos de trabajo.

Para un uso más avanzado, consulte las secciones [ASFSearchResults class](/asf_search/ASFSearchResults/) y [ASFProduct class](/asf_search/ASFProduct).

## Palabras clave

Las palabras clave se utilizan para encontrar los datos deseados. Use tantas o tan pocas palabras clave como sea necesario. Las palabras clave y descripciones disponibles se enumeran a continuación. Además, se proporcionan numerosas constantes para facilitar el proceso de búsqueda. Actualmente, proporcionamos constantes para el modo de haz, la dirección de vuelo, el instrumento, la plataforma, la polarización y el tipo de producto. Puedes ver la [lista completa de constantes aquí](https://github.com/asfadmin/Discovery-asf_search/tree/master/asf_search/constants).

### Parámetros del conjunto de datos
- <span style="color: #236192; tamaño de fuente: 20px;" >plataforma</span>
    - Consulte la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/PLATFORM.py)
    - Plataforma de teledetección que adquirió los datos. Sentinel-1 y ERS tienen múltiples plataformas de teledetección, y usted puede elegir si desea especificar una plataforma específica. Puede especificar un solo valor o una lista de valores.
    - También puede obtener la lista disponible de constantes usando '''help(asf_search.constants.PLATFORM)'''
    -Ejemplo:
        - plataforma=asf. PLATAFORMA. SENTINEL1A

- <span style="color: #236192; tamaño de fuente: 20px;" >instrumento</span>
    - Consulte la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/INSTRUMENT.py)
    - Instrumento de teledetección que adquirió los datos. Para algunas plataformas, como ALOS, hay varios instrumentos para elegir.
    - También puede obtener la lista disponible de constantes usando '''help(asf_search.constants.INSTRUMENT)'''
    -Ejemplo:
        - instrumento=asf. INSTRUMENTO. AVNIR_2

- <span style="color: #236192; tamaño de fuente: 20px;" >absoluteBurstID</span>
    - Utilizado para Sentinel-1 [productos de ráfaga](/datasets/using_ASF_data/#sentinel-1-bursts). Cada valor identifica la pila de un ciclo de ráfaga, representando todos los productos generados en una subfranja específica. Puede especificar un solo valor o una lista de valores. 
    -Ejemplo:
        - valor único: absoluteBurstID='102563902'
        - lista de valores: absoluteBurstID=['102563902', '103558145']

- <span style="color: #236192; tamaño de fuente: 20px; tamaño de fuente: 20px;" >absoluteOrbit</span>
    - Para ALOS, ERS-1, ERS-2, JERS-1, RADARSAT-1, Sentinel-1A y Sentinel-1B, este valor corresponde al recuento de órbitas dentro del ciclo orbital. Para UAVSAR es el [ID de vuelo](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.34282209.1335434931.1620087198-1930115146.1605056035). Puede especificar un solo valor, un rango de valores o una lista de valores.
    -Ejemplo:
        - valor único: absoluteOrbit=25436
        - rango de valores: absoluteOrbit=(12005, 12008)
        - lista de valores: absoluteOrbit=[25436, 25450]  

- <span style="color: #236192; tamaño de fuente: 20px;" >asfFrame</span>
    - Véase también 'marco'
    - Esto es principalmente una referencia de marco ASF / [JAXA] (https://global.jaxa.jp/). Sin embargo, algunas plataformas utilizan otras convenciones. Puede especificar un solo valor, un rango de valores o una lista de valores.
    -Ejemplo:
        - valor único: asfFrame = 300
        - rango de valores: asfFrame = (2845, 2855)
        - lista de valores: asfFrame=[2800, 2845]
    -Valores:
        - ERS, JERS, RADARSAT: tramas ASF 0 a 900
        - ALOS PALSAR: JAXA fotogramas 0 a 7200
        - SEASAT: cuadros tipo ESA 208 a 3458
        - Sentinel-1: Valores internos de 0 a 1184

- <span style="color: #236192; tamaño de fuente: 20px;" >beamMode</span>
    - Consulte la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/BEAMMODE.py)
    - El modo de haz utilizado para adquirir los datos.
    - También puede obtener la lista disponible de constantes usando '''help(asf_search.constants.BEAMMODE)'''
    -Ejemplo:
        - beamMode=asf. BEAMMODE. POL

- <span style="color: #236192; tamaño de fuente: 20px;" >beamSwath</span>
    - La franja de haz abarca un ángulo de mirada y un modo de haz. Puede especificar un solo valor o una lista de valores.
    -Ejemplo:
        - valor único: beamSwath='IW'
        - lista de valores: beamSwath=['IW','EW']

- <span style="color: #236192; tamaño de fuente: 20px;" >campaña</span>
    - Solo para conjuntos de datos de UAVSAR, AIRSAR y Sentinel-1 Interferogram. Busca por el nombre de la campaña. Puede especificar un único valor.
    - Para obtener una lista de las campañas disponibles, utilice la función '''asf_search.campaigns()'''. Debe proporcionar la plataforma deseada.
        - '''asf_search.campañas(asf_search. PLATAFORMA. UAVSAR)'''
    -Ejemplo:
        - campaign='Volcán Purac, Colombia'

- <span style="color: #236192; tamaño de fuente: 20px;" >maxDoppler</span>
    Doppler proporciona una indicación de cuánto se desvía la dirección de la mirada de la adquisición ideal de la dirección de vuelo perpendicular.
    -Ejemplo:
        - maxDoppler=1500 o maxDoppler=1500.5

- <span style="color: #236192; tamaño de fuente: 20px;" >minDoppler</span>
    Doppler proporciona una indicación de cuánto se desvía la dirección de la mirada de la adquisición ideal de la dirección de vuelo perpendicular.
    -Ejemplo:
        - minDoppler=100 o minDoppler=1500.5

- <span style="color: #236192; tamaño de fuente: 20px;" >maxFaradayRotation</span>
    - La rotación del plano de polarización de la señal de radar impacta las imágenes. Las señales HH y HV se mezclan. Es probable que las rotaciones unidireccionales superiores a 5° reduzcan significativamente la precisión de la recuperación de parámetros geofísicos, como la biomasa forestal.
    -Ejemplo:
        - maxFaradayRotation=3.5

- <span style="color: #236192; tamaño de fuente: 20px;" >minFaradayRotation</span>
    - La rotación del plano de polarización de la señal de radar impacta las imágenes. Las señales HH y HV se mezclan. Es probable que las rotaciones unidireccionales superiores a 5° reduzcan significativamente la precisión de la recuperación de parámetros geofísicos, como la biomasa forestal.
    -Ejemplo:
        - minFaradayRotation=2

- <span style="color: #236192; tamaño de fuente: 20px;" >flightDirection</span>
    - Ver la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/FLIGHT_DIRECTION.py)
    - Dirección de la órbita del satélite durante la adquisición de datos. Puede especificar un único valor.
    - También puede obtener la lista disponible de constantes usando '''help(asf_search.constants.FLIGHT_DIRECTION)'''
    -Ejemplo:
        - flightDirection=asf. FLIGHT_DIRECTION. ASCENDENTE

- <span style="color: #236192; tamaño de fuente: 20px;" >flightLine</span>
    - Especifique una línea de vuelo para UAVSAR o AIRSAR. Puede especificar un único valor.
    -Ejemplo:
        - UAVSAR: flightLine='05901'
        - AIRSAR: flightLine='gilmorecreek045-1.93044'

- <span style="color: #236192; tamaño de fuente: 20px;" >marco</span>
    - Véase también 'asfFrame'
    - Se ofrecen marcos referenciados por la ESA para ofrecer a los usuarios una convención de encuadre universal. Cada trama ESA tiene asignada una trama ASF correspondiente. Puede especificar un solo valor, un rango de valores o una lista de valores.
    -Ejemplo:
        - Valor único: fotograma = 300
        - Rango de valores: frame=(305, 315)
        - Lista de valores: frame=[300, 303, 305]
    -Valores:
        - Cualquier número de 0 a 7200.

- <span style="color: #236192; tamaño de fuente: 20px;" >fullBurstID</span>
    - Utilizado para Sentinel-1 [productos de ráfaga](/datasets/using_ASF_data/#sentinel-1-bursts). Cada valor representa todos los productos de ráfaga en una sola subfranja, correspondiente a una pila alineada con el marco casi perfecta. Este valor es útil para el apilamiento de línea base. Puede especificar un solo valor o una lista de valores.
    -Ejemplo:
        - valor único: fullBurstID='017_034465_IW2'
        - lista de valores: fullBurstID=['017_034465_IW2', '079_167884_IW1']

- <span style="color: #236192; tamaño de fuente: 20px;" >groupID</span>
    - Lista de ID de grupos específicos. Para algunos datasets, el ID de grupo es el mismo que el nombre de la escena. Para otros, como Sentinel-1, el ID de grupo es único para un grupo de escenas.
    -Ejemplo:
        - groupID='S1A_IWDV_0112_0118_037147_150'

- <span style="color: #236192; tamaño de fuente: 20px;" >lookDirection</span>
    - Dirección izquierda o derecha de adquisición de datos. Puede especificar un único valor.
    -Ejemplo:
        - lookDirection='L'
    -Valores:
        - R, DERECHA, L, IZQUIERDA

- <span style="color: #236192; tamaño de fuente: 20px;" >offNadirAngle</span>
    - Ángulos fuera del nadir para ALOS PALSAR. Puede especificar un solo valor, un rango de valores o una lista de valores.
    -Ejemplo:
        - valor único: offNadirAngle=21.5
        - rango de valores: offNadirAngle=(9.7, 14)
        - lista de valores: offNadirAngle=[21.5, 23.1]
    -Valores:
        - Más comunes: 21.5, 23.1, 27.1, 34.3
        - Otros: 9.7, 9.9, 13.8, 14, 16.2, 17.3, 17.9, 18, 19.2, 20.5, 21.5, 23.1, 24.2, 24.6, 25.2, 25.8, 25.9, 26.2, 27.1, 28.8, 30.8, 34.3, 36.9, 38.8, 41.5, 43.4, 45.2, 46.6, 47.8, 49, 50, 50.8

- <span style="color: #236192; tamaño de fuente: 20px;" >polarización</span>
    - Ver la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/POLARIZATION.py)
    - Una propiedad de las ondas electromagnéticas SAR que se puede utilizar para extraer información significativa sobre las propiedades de la superficie de la tierra. Puede especificar un solo valor o una lista de valores.
    - También puede obtener la lista disponible de constantes usando '''help(asf_search.constants.POLARIZATION)'''
    -Ejemplo:
        - polarización = PPA. POLARIZACIÓN. VV

- <span style="color: #236192; tamaño de fuente: 20px;" >processingLevel</span>
    - Ver la [lista de constantes](https://github.com/asfadmin/Discovery-asf_search/blob/master/asf_search/constants/PRODUCT_TYPE.py)
    - Nivel al que se han tratado los datos, también tipo de producto.
    - También puede obtener la lista disponible de constantes usando '''help(asf_search.constants.PRODUCT_TYPE)'''
    -Ejemplo:
        - processingLevel=asf. PRODUCT_TYPE. SLC

- <span style="color: #236192; tamaño de fuente: 20px;" >relativeBurstID</span>
    - Utilizado para Sentinel-1 [productos de ráfaga](/datasets/using_ASF_data/#sentinel-1-bursts). Cada valor identifica un ciclo de ráfaga, y dentro de cada subfranja estos valores son únicos. Puede especificar un solo valor o una lista de valores.
    -Ejemplo:
        - valor único: relativeBurstID='367299'
        - lista de valores: relativeBurstID=['167877', '167882']

- <span style="color: #236192; tamaño de fuente: 20px;" >relativeOrbit</span>
    - Ruta o seguimiento del satélite durante la adquisición de datos. Para UAVSAR es el [ID de línea](https://uavsar.jpl.nasa.gov/cgi-bin/data.pl?_ga=2.201268782.1252483948.1620685771-1930115146.1605056035). Puede especificar un solo valor, un rango de valores o una lista de valores.
    -Ejemplo:
        - valor único: relativeOrbit=5905
        - rango de valores: relativeOrbit=(2400, 2410)
        - lista de valores: relativeOrbit=[500, 580]
    -Valores:
        - ALOS: 1-671
        - ERS-1: 0-2410
        - ERS-2: 0-500
        - JERS-1: 0-658
        - RADARSAT-1: 0-342
        - SEASAT: 1-243
        - UAVSAR: varios

### Parámetros geoespaciales

- <span style="color: #236192; tamaño de fuente: 20px;" >intersectsWith</span>
    - Búsqueda por polígono, un segmento de línea ("linestring"), o un punto definido en 2-D Well-Known Text (WKT). Cada polígono debe estar explícitamente cerrado, es decir, el primer vértice y el último vértice de cada polígono enumerado deben ser idénticos. Los pares de coordenadas para cada vértice están en grados decimales: la longitud es seguida por la latitud.
    -Ejemplo:
        - intersectsWith='POLÍGONO((-152,81 58,49,-154,90 57,49,-155,08 56,30,-153,82 56,34,-151,99 57,30,-151,43 58,19,-152,81 58,49))'
        - intersectsWith='LINESTRING(-119.543 37.925, -118.443 37.7421)'
        - intersectsWith='PUNTO(-119.543 37.925)'

#### Validación de formas
Si la AOI especificada es su propio rectángulo delimitador mínimo (MBR) en una proyección de Mercator, los resultados de la búsqueda devueltos se integrarán con la AOI en una proyección de Mercator, independientemente de la anchura. Este sigue siendo el caso incluso si la línea de fecha internacional se cruza dentro del AOI.

Para que un AOI se considere su propio MBR, debe cumplir con los siguientes criterios:

  - Cada vértice comparte una latitud o longitud con sus vecinos
  - Los puntos Este/Oeste comparten longitud
  - Los puntos Norte/Sur comparten latitud

Los AOI que no se ajusten a este criterio tendrán sus puntos conectados a lo largo de [grandes círculos] (https://en.wikipedia.org/wiki/Great_circle).

Además, todos los AOI se validan y luego se simplifican según sea necesario. El proceso para esto es:
 
  1. Valide el AOI de entrada. Si no es válido, se muestra un error.
  2. Fusionar formas superpuestas.
  3. Casco convexo.
  4. Cualquier valor de índice fuera de rango se maneja sujetándolos y envolviéndolos en el rango válido de valores.
  5. Simplifique los puntos en función del umbral de proximidad. El objetivo es menos de 400 puntos.

Cada uno de estos pasos se realiza solo cuando es necesario para obtener el AOI a un solo esquema con menos de 400 puntos. Se omiten los pasos innecesarios.

**Ejemplos de validación y simplificación:**

- Se proporciona un polígono de autointersección: 
    - Se muestra un error.
- Se proporciona un esquema único, que consta de 1000 puntos:
    - Se utiliza una versión simplificada del mismo esquema, que consta de menos de 400 puntos.
- Se proporcionan múltiples geometrías, todas ellas superpuestas al menos en parte:
    - Se devuelve un solo contorno, que representa el contorno de todas las formas combinadas.
- Se proporcionan múltiples geometrías, al menos algunas de ellas totalmente no superpuestas:
    - Se devuelve un solo contorno, que representa el casco convexo de todas las formas juntas.

### Parámetros temporales
- <span style="color: #236192; tamaño de fuente: 20px;" >processingDate</span>
    - Limitar los resultados a los registros que se han procesado en ASF desde una fecha y/u hora determinada.
    -Ejemplo:
        - processingDate='2017-01-01T00:00:00UTC'

- <span style="color: #236192; tamaño de fuente: 20px;" >inicio</span>
    - Fecha de adquisición de los datos. Se puede utilizar en combinación con 'end'. Puede introducir fechas en lenguaje natural o una marca de fecha y/o hora. Todos los horarios están en UTC.
    -Ejemplo:
        - start='30 de mayo de 2019'
        - start='ayer'
        - inicio='2010-10-30T11:59:59Z'
        - start='hace 1 semana', end='ahora'

- <span style="color: #236192; tamaño de fuente: 20px;" >fin</span>
    - Fecha de adquisición de los datos. Se puede utilizar en combinación con 'start'. Puede introducir fechas en lenguaje natural o una marca de fecha y/o hora. Todos los horarios están en UTC.
        - end='30 de mayo de 2018'
        - end='hoy'
        - end='2021-04-30T11:59:59Z'
        - start='hace 1 semana', end='ahora'

- <span style="color: #236192; tamaño de fuente: 20px;" >temporada</span>
    - Día de inicio y finalización del año para el rango estacional deseado. Esta palabra clave se puede usar junto con inicio/fin para especificar un rango estacional dentro de un rango de fechas general. Los valores se basan en el calendario juliano. Debe especificar una fecha de inicio y finalización de la temporada.
    -Ejemplo:
        - temporada=[1, 31]
        - temporada=[45, 67]
        - temporada=[360, 10]
    -Valores:
        - 1 a 365

### Parámetros de línea base
- <span style="color: #236192; tamaño de fuente: 20px;" >stack_from_id</span>
    - Introduzca el nombre de la escena para la que desea ver los resultados de línea base.
    - stack_from_id no se puede utilizar en conjunción con otras palabras clave.
    -Ejemplo: 
        - stack_from_id('S1A_IW_SLC__1SDV_20220215T225119_20220215T225146_041930_04FE2E_9252-SLC')
    - Consulte el [bloc de notas de Jupyter](https://github.com/asfadmin/Discovery-asf_search/blob/master/examples/4-Baseline_Search.ipynb) para obtener ejemplos de uso, así como procedimientos recomendados.

### Parámetros de resultados
- <span style="color: #236192; tamaño de fuente: 20px;" >maxResults</span>
    - Número máximo de registros de datos a devolver.
    -Ejemplo:
        - maxResults=10

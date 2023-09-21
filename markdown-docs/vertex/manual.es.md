# Guía de Inicio de Vertex

- Si aún no tienes una cuenta gratuita de **[Earthdata Login](https://urs.earthdata.nasa.gov/users/new)**, créala.
- Ve a **[Vertex](https://search.asf.alaska.edu)**
	- Inicia sesión haciendo clic en el ícono de **Iniciar sesión** en la esquina superior derecha de la ventana. Utiliza tu nombre de usuario y contraseña de Earthdata Login.
	![tipo:video](https://www.youtube.com/embed/j_Db_ipKLos)
- El tipo de búsqueda te permite elegir entre todos los tipos de búsqueda disponibles.

## Opciones de Idioma

En el menú en la esquina superior derecha, junto al ícono de **Iniciar sesión**, hay opciones de control de idioma. Vertex actualmente ofrece inglés y español. Si tu navegador está configurado en uno de los idiomas disponibles, Vertex se ajustará automáticamente a ese idioma. Puedes hacer clic en el botón y seleccionar tu idioma deseado en la lista desplegable. También puedes establecer un idioma predeterminado en tus **Preferencias**.

## Opciones de Búsqueda *Geográfica*

![tipo:video](https://www.youtube.com/embed/JovQ-rG9ZJE)

- En la esquina superior izquierda del mapa, hay botones que te permiten cambiar tu **proyección de mapa**, **zoom** y **vista de mapa**.
	- Por defecto, el mapa está en proyección ecuatorial. Puedes hacer clic en **Vista de mapa** y seleccionar **Vista de mapa ártico** o **Vista de mapa antártico** para cambiar la proyección del mapa. Haz clic en **Vista de mapa ecuatorial** para volver a la proyección ecuatorial.
	- Puedes hacer clic en los íconos de **Acercar** o **Alejar** para ajustar el zoom.
	- La capa de mapa por defecto es satélite. Puedes hacer clic en el botón **Capas** y seleccionar **Vista de satélite** o **Vista de calle** para cambiar la capa de mapa.
		- Puedes hacer clic en **Mapa de resumen** para agregar un mapa de resumen en la esquina superior derecha del mapa. Haz clic nuevamente para desactivar el mapa de resumen.
		- Puedes hacer clic en **Líneas de cuadrícula** para agregar una superposición de graticule al mapa. Haz clic nuevamente para desactivar la superposición. *Nota*: Esto actualmente solo está disponible en la vista de mapa ecuatorial.
	- Puedes hacer clic en **Opacidad** y ajustar el deslizador según desees para cambiar la opacidad de las imágenes de navegación que se muestran en el mapa.
- Navega hasta tu área de interés arrastrando el mapa mientras mantienes presionado el botón izquierdo del mouse.
- Por defecto, la herramienta de dibujo en el mapa es un cuadro delimitador. Haz clic en el mapa una vez para especificar la esquina inicial, mueve el mouse y luego haz clic nuevamente para terminar el cuadro. Hay opciones adicionales de herramientas de dibujo disponibles en la barra de herramientas en la parte superior de la pantalla, que incluyen opciones de *punto*, *línea* y *polígono*.
	- **Punto** te permite definir un área de interés haciendo clic en el mapa para colocar un punto.
	- **Línea** te permite definir un área de interés sobre una serie de segmentos de línea haciendo clic en el mapa varias veces. Haz doble clic para detener la adición de segmentos.
	- **Polígono** te permite definir un área de interés sobre un polígono arbitrario. Recibirás un mensaje de error en la parte inferior de la ventana si hubo algún problema con el polígono (autointersección, orden inverso del polígono, etc.).
	- **Cuadro** te permite definir un área de interés sobre un cuadro delimitador alineado con latitud/longitud haciendo clic una vez para establecer una esquina y nuevamente para establecer la esquina opuesta.
	- Una vez que se haya dibujado una forma, selecciona el ícono de **Editar área de interés actual** en la barra de herramientas para mover, agregar y eliminar puntos. Selecciona el ícono de **Dibujar nueva área de interés** para crear una nueva AOI.
	- Hacer clic en **Cargar archivo geoespacial** abre la ventana de diálogo de Área de interés. Puedes ingresar una cadena WKT, cargar un archivo geoespacial o ingresar una ubicación.
- **Conjunto de datos** te permite elegir el conjunto de datos de interés.
	- Si necesitas más información sobre un conjunto de datos en particular, haz clic en el ícono de interrogación correspondiente en el selector de Conjunto de datos.
- **Filtros...** te permite refinar aún más tu búsqueda

### Opciones de Área de Interés

- **Área de Interés** te brinda la opción de ingresar un conjunto de coordenadas geográficas, importar un área de interés como un archivo geoespacial o buscar una ubicación. Haz clic en la flecha hacia abajo junto a **Área de Interés** en el menú superior.
	- Un área de interés se puede definir mediante un conjunto de coordenadas ingresadas en la ventana **Área de Interés WKT**.
		- Las coordenadas deben ingresarse en grados decimales en formato *texto bien conocido* (WKT). Las coordenadas ingresadas como una cadena de longitud/latitud separadas por comas (por ejemplo, -97.38,36.46,-53.44,36.46...) se convertirán automáticamente a formato WKT por Vertex.
	- Para cargar un archivo geoespacial, haz clic en **Seleccionar archivos** y navega hasta una carpeta en tu computadora o arrastra y suelta archivos en el cuadro. Se admiten archivos *GeoJSON*, *shapefiles* y *KML* siempre que estén en un sistema de coordenadas basado en latitud/longitud, como WGS84.
		- Al importar un archivo *GeoJSON*, se incluirán todas las geometrías en el archivo. Si se encuentran múltiples geometrías, se utilizará una envolvente convexa para representarlas en la búsqueda.
		- Los *shapefiles* pueden ser un solo archivo *.shp*, múltiples componentes de archivo shapefile (*.shp, .shx, .dbf*), o un archivo *zip* que contenga uno o más componentes de archivo shapefile. En todos los casos, se debe incluir como mínimo el componente *.shp*.
	- Para ingresar una ubicación, haz clic en el campo **Buscar una ubicación** y comienza a escribir el nombre de la ubicación. Selecciona la ubicación deseada en la lista desplegable. 
		- Una vez que hayas seleccionado una ubicación, se convertirá en coordenadas en formato WKT.
	- Puedes guardar las coordenadas de una búsqueda para poder recrear exactamente un área de interés en búsquedas posteriores.
		- Una vez que se haya configurado el **Área de Interés**, aparecerá un ícono de *Copiar al portapapeles*. Haz clic en el ícono y pega las coordenadas en una nueva búsqueda o en un archivo de texto para usarlas más tarde.
		- Nota: Consulta la sección **Otras Opciones de Vertex** para conocer formas adicionales de guardar búsquedas.
	- En cualquier momento, puedes borrar tu área de búsqueda haciendo clic en el botón **Borrar**.

#### Validación de Forma
Si el AOI especificado es su propio Rectángulo Mínimo Delimitador (MBR) en una proyección mercator, los resultados de la búsqueda devueltos se intersectarán con el AOI en una proyección mercator, independientemente del ancho. Esto sigue siendo válido incluso si la línea de cambio de fecha internacional se cruza dentro del AOI.

Para que un AOI se considere su propio MBR, debe cumplir con los siguientes criterios:

  - Cada vértice comparte una latitud o longitud con sus vecinos
  - Los puntos Este/Oeste comparten longitud
  - Los puntos Norte/Sur comparten latitud

AOIs que no cumplan con estos criterios tendrán sus puntos conectados a lo largo de [círculos máximos](https://es.wikipedia.org/wiki/C%C3%ADrculo_m%C3%A1ximo).

Además, todos los AOIs se validan y se simplifican según sea necesario. El proceso para ello es:

  1. Validar el AOI de entrada. Si no es válido, se mostrará un error.
  2. Fusionar formas superpuestas.
  3. Envoltura convexa.
  4. Cualquier valor de índice fuera de rango se maneja mediante la restricción y el ajuste a la gama de valores válidos.
  5. Simplificar puntos según el umbral de proximidad. El objetivo es tener menos de 400 puntos.

Cada uno de estos pasos se realiza solo cuando es necesario para obtener el AOI con un solo contorno con menos de 400 puntos. Cualquier paso innecesario se omite.

**Ejemplos de validación y simplificación:**

- Se proporciona un polígono que se interseca a sí mismo:
- Se muestra un error.
- Se proporciona un esquema único, compuesto por 1000 puntos:
- Se utiliza una versión simplificada del mismo esquema, compuesta por menos de 400 puntos.
- Se proporcionan múltiples geometrías, superponiéndose todas ellas al menos en parte:
- Se devuelve un único contorno, que representa el contorno de todas las formas combinadas.
- Se proporcionan múltiples geometrías, al menos algunas de ellas no se superponen en absoluto:
- Se devuelve un contorno único, que representa el casco convexo de todas las formas juntas.

### Filtros de fecha

- **Filtros de fechas** Las fechas de búsqueda son opcionales, por lo que están vacías de forma predeterminada. Si está buscando fechas específicas, puede definir más el rango de fechas en los campos **Fecha de inicio** y **Fecha de finalización**. El selector de fechas limitará automáticamente su selección a un rango válido para el conjunto de datos seleccionado.
- *Nota*: esta información también se puede encontrar haciendo clic en el icono del signo de interrogación de un conjunto de datos.
- **Búsqueda estacional** permite restringir la búsqueda a ciertos períodos anuales dentro de un rango general de fechas. Haga clic en el botón de búsqueda de temporada y aparecerán opciones adicionales que le permitirán ingresar un rango de fechas general (*Fecha de inicio/Fecha de finalización*) y el rango estacional (*Día de inicio de temporada/Día de finalización de temporada*).

### Filtros adicionales

![tipo:vídeo](https://www.youtube.com/embed/Vd9eDL9KVK4)

- **Filtros adicionales** permiten aplicar parámetros adicionales para limitar su búsqueda y reducir la cantidad de resultados. No todos los filtros estarán disponibles para todos los conjuntos de datos.
- **Tipo de archivo**: limita la búsqueda a tipos específicos de archivos. Se permiten múltiples selecciones.
- **Modo de haz**: limita la búsqueda a modos de haz específicos. Se permiten múltiples selecciones.
- **Polarización** – Limita la búsqueda a polarizaciones específicas. Se permiten múltiples selecciones.
- **Dirección**: limita la búsqueda a una dirección orbital específica.
- **Subtipo**: limita la búsqueda a una nave espacial de misión específica.

### Filtros de ruta y marco

- **Filtros de ruta y marco** están disponibles para conjuntos de datos seleccionados. Puede ingresar una única ruta o marco, o un rango. Debido a la inconsistencia del encuadre de Sentinel-1, recomendamos buscar un cuadro de interés entre ±1 y 2 cuadros.
- El número máximo de resultados se muestra debajo del botón **BUSCAR**. Haga clic en la **flecha hacia abajo** para elegir los resultados máximos que prefiera.
- Puede hacer clic en **URL de API...** para generar la URL de API que coincida con sus parámetros de búsqueda actuales. Esto abrirá una nueva ventana.
- **Cantidad** le permite establecer los resultados máximos.
- **Formato** le permite elegir su formato de salida preferido.
- El icono **Copiar** junto a la URL copiará la URL. Se puede pegar en la barra de búsqueda del navegador para realizar la búsqueda API, o pegarlo en un documento y guardarlo.
- **API Docs** lo enviará a la [Documentación de API](https://asf.alaska.edu/api/).
- **Descargar resultados** descargará los resultados en el formato de salida especificado.
- Una vez elegidos todos los parámetros, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán en el área del pie de página de la ventana de Vertex y en el mapa.
- *Nota*: El número de archivos que se prevé que coincidan con los parámetros de búsqueda actuales se muestra debajo del botón BUSCAR. Si no hay coincidencias previstas, el botón de búsqueda aparecerá atenuado y mostrará SIN RESULTADOS.


## *Lista* Opciones de búsqueda

![tipo:vídeo](https://www.youtube.com/embed/oetqxZkqVZM)

- Al seleccionar **Búsqueda de lista** se abre la ventana *Búsqueda de lista* y le permite ingresar una lista de escenas o nombres de archivos.
- **Escena** permite buscar nombres de escenas específicas (nombres de gránulos) y los resultados incluirán cualquier archivo que forme parte de esas escenas.
- **Archivo** permite buscar nombres de archivos específicos (nombres de productos) y los resultados solo incluirán exactamente esos archivos.
- **Editar lista** abre la ventana *Búsqueda de lista* para que puedas realizar cambios en tu lista
- Una vez elegidos todos los parámetros, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán en el área del pie de página de la ventana de su navegador y en el mapa.
- *Nota*: El número de archivos que se prevé que coincidan con los parámetros de búsqueda actuales se muestra debajo del botón BUSCAR. Si no hay coincidencias previstas, el botón de búsqueda aparecerá atenuado y mostrará NO HAY RESULTADOS.

### Importación de archivos de búsqueda de listas
Puede **arrastrar y soltar archivos** en el cuadro provisto en las pestañas **Escena** o **Archivo**. Cada pestaña enumera los tipos de archivos aceptados en la parte inferior. Vertex analizará la escena o los nombres de los archivos del archivo cargado.

- *Nota*: Cada tipo de archivo requiere un formato específico. Los archivos exportados desde Vertex tendrán el formato correcto.

- **CSV** requiere una columna denominada "Nombre de granulo" para una búsqueda en la lista de escenas. Requiere una columna adicional de "Nivel de procesamiento" para una búsqueda en la lista de archivos.
- **GeoJSON** requiere un campo denominado "granuleName" para la búsqueda en la lista de escenas. Requiere un campo denominado "fileID" para la búsqueda en la lista de archivos.
- **Metalink** requiere una estructura formateada como
```

<enlace metálico>
    <archivos>
        <nombre de archivo="[Nombre-escena.zip]"></archivo>
        <nombre de archivo="...
        ...</archivo>
    </archivos>
</metalink>
```

- **KML** requiere una estructura formateada como
```
<kml>
    <Documento>
        <Marca de posición>
            <nombre>[Nombre de la escena]</nombre>
        </marca de posición>
    </Documento>
</kml>
```

## *Línea base* Opciones de búsqueda

![tipo:vídeo](https://www.youtube.com/embed/Xp5bgvi2pEM)

## *Línea base* Opciones de búsqueda

![tipo:vídeo](https://www.youtube.com/embed/Xp5bgvi2pEM)

- Seleccionar **Búsqueda de línea base** proporciona un espacio para ingresar el nombre de una escena de referencia y luego buscará todas las escenas secundarias que coincidan con el área de cobertura de la referencia.
- *Nota*: Si no hay escenas coincidentes, el botón RESULTADOS estará atenuado y mostrará SIN RESULTADOS.
- Una vez que se haya ingresado una escena de referencia, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán debajo del mapa. Al hacer clic en el ícono *Acercar a los resultados* en la parte superior de la columna de resultados de la izquierda, se mostrará la ubicación de la pila de escenas en el mapa.
- El gráfico muestra la relación Temporal y Perpendicular (espacial) de las escenas secundarias a la Referencia.
- Al hacer clic en **Criterios de referencia...** encima del gráfico, se abrirá la ventana *Búsqueda de referencia*. Usando los controles deslizantes, las extensiones Temporal y Perpendicular se pueden ajustar para limitar la cantidad de escenas secundarias que se muestran en los resultados.
- Para obtener más información sobre **Baseline**, consulte la [Documentación de Baseline](/vertex/baseline).

## *SBAS* Opciones de búsqueda

![tipo:vídeo](https://www.youtube.com/embed/bQPdtuobdcg)

- Seleccionar **Búsqueda de línea base** proporciona un espacio para ingresar el nombre de una escena de referencia y luego buscará todas las escenas secundarias que coincidan con el área de cobertura de la referencia.
- *Nota*: Si no hay escenas coincidentes, el botón RESULTADOS estará atenuado y mostrará SIN RESULTADOS.
- Una vez que se haya ingresado una escena de referencia, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán debajo del mapa. Al hacer clic en el ícono *Acercar a los resultados* en la parte superior de la columna de resultados de la izquierda, se mostrará la ubicación de la pila de escenas en el mapa.
- El gráfico muestra la relación Temporal y Perpendicular (espacial) de las escenas secundarias a la Referencia.
- Al hacer clic en **Criterios de referencia...** encima del gráfico, se abrirá la ventana *Búsqueda de referencia*. Usando los controles deslizantes, las extensiones Temporal y Perpendicular se pueden ajustar para limitar la cantidad de escenas secundarias que se muestran en los resultados.
- Para obtener más información sobre **Baseline**, consulte la [Documentación de Baseline](/vertex/baseline).

## *SBAS* Opciones de búsqueda

![tipo:vídeo](https://www.youtube.com/embed/bQPdtuobdcg)

- Seleccionar **Búsqueda SBAS** proporciona un espacio para ingresar el nombre de una Escena de Referencia y buscará todas las escenas secundarias que coincidan con el área de cobertura de la Referencia. Es un método alternativo utilizado para el procesamiento de SAR interferométrico (InSAR), similar a Baseline.
- *Nota*: Si no hay escenas coincidentes, el botón RESULTADOS estará atenuado y mostrará SIN RESULTADOS.
- Una vez que se haya ingresado una escena de referencia, haga clic en **BUSCAR**. Los resultados de la búsqueda aparecerán debajo del mapa. Al hacer clic en el ícono *Acercar a los resultados* en la parte superior de la columna de resultados de la izquierda, se mostrará la ubicación de la pila de escenas en el mapa.
- El gráfico muestra la relación Temporal y Perpendicular (espacial) de las escenas secundarias con la Referencia.
- Los botones **Acercar** y **Alejar** están disponibles encima del gráfico.
- El botón **Acercar para ajustar** garantiza que todos los pares sean visibles en el gráfico.
- Los botones **Par personalizado** le permiten agregar o eliminar un par personalizado.
- El botón **Criterios SBAS...** le permite especificar criterios adicionales para refinar sus resultados, como fechas de inicio y finalización, configuraciones de fechas estacionales y configuraciones de umbrales de superposición latitudinal.
- Para obtener más información sobre **SBAS**, consulte la [documentación de SBAS](/vertex/sbas).

## *Productos bajo demanda* Opciones de búsqueda

- Seleccionar **Productos On Demand** le permite ver los trabajos On Demand enviados. *Nota*: Debes iniciar sesión para acceder a esto. Si no ha iniciado sesión, esta opción de búsqueda aparecerá atenuada y no podrá seleccionarla.
- **Nombre del proyecto** le permite limitar su búsqueda a un nombre de proyecto específico. A medida que comience a escribir, las opciones de autocompletar estarán disponibles con los nombres de los proyectos que haya utilizado anteriormente.
- **Filtros de fechas** Las fechas de búsqueda son opcionales, por lo que están vacías de forma predeterminada. Si está buscando fechas específicas, puede definir más el rango de fechas en los campos **Fecha de inicio** y **Fecha de finalización**. *Nota*: Estas fechas se filtran por la fecha de la escena, no por la fecha en que se procesó.
- **Producto/Escena de origen** le permite ingresar el nombre del producto o el nombre de la escena de origen para limitar su búsqueda. Este campo también aceptará una cadena parcial del producto o de la escena fuente en lugar del nombre completo.
- **Estado del trabajo** le permite limitar su búsqueda a estados específicos. Se permiten múltiples selecciones.
- *Nota*: Los trabajos caducan 14 días después de enviarlos. Los productos caducados aún aparecen en los resultados de búsqueda; sin embargo, ya no podrá descargarlos ni agregarlos a su carrito. Puede identificar fácilmente sus productos caducados mediante la etiqueta **Caducado** junto al nombre del producto.
- Para obtener más información sobre **Productos On Demand**, consulte la [documentación](https://hyp3-docs.asf.alaska.edu/).

## *Conjuntos de datos derivados* Opciones de búsqueda

- Seleccionar **Conjuntos de datos derivados** le permite ver y descargar productos del catálogo de conjuntos de datos de ASF.
- Cada conjunto de datos enumerado incluye una breve descripción.
- Haga clic en **Más información** para ver más información sobre el conjunto de datos.
- Haga clic en **Descargar** para ver y descargar los productos disponibles para el conjunto de datos elegido. *Nota*: El enlace de descarga se abrirá en una nueva ventana del navegador.
- Para obtener más información sobre **Conjuntos de datos derivados**, consulte la [documentación de conjuntos de datos derivados](/vertex/derived_datasets/).

## Resultados de la búsqueda

![tipo:vídeo](https://www.youtube.com/embed/wp8Xt_Y4T84)

- En Vertex, una **escena** se considera un paquete que contiene todos los **archivos** o productos relacionados con una ubicación y un tiempo específicos.
        - *Por ejemplo*, la columna a la izquierda del panel Resultados muestra las escenas devueltas por una búsqueda. La columna de la derecha muestra el contenido del archivo de cada escena.
   - La cantidad máxima de archivos que arrojará una búsqueda se muestra debajo del botón BÚSQUEDA.
   - Este número se puede ajustar haciendo clic en la flecha hacia abajo.
- También se muestra el número total de archivos que coinciden con los parámetros de búsqueda.
- La barra de encabezado de Resultados.
 - El botón **Zoom** acercará la ubicación de todas las escenas en el mapa.
 - El botón **Cola** agregará todas las escenas a la cola de descarga.
 - El botón **On Demand** le permitirá elegir qué escenas elegibles agregar a la cola On Demand para su posterior procesamiento.
 - El botón **Raw** mostrará u ocultará archivos sin formato. *Nota*: Este botón solo se aplica a escenas Sentinel-1.
 - El botón **Exportar** le permitirá exportar datos o metadatos para todas las escenas en los resultados.
 - El botón **Caducado** mostrará u ocultará los archivos On Demand caducados.  *Nota*: Este botón solo está disponible en el tipo de búsqueda **Productos On Demand**.
  - *Nota*: No todos los botones están disponibles en todos los tipos de búsqueda.
- La columna **Escenas** (izquierda).
           - Haga clic en el ícono del carrito al lado del nombre de una escena para agregar todos los archivos de la escena a la cola de descarga. El carrito cambia de apariencia cuando se hace esto.
            - Haga clic en el icono de zoom junto al nombre de una escena para acercar la ubicación de la escena en el mapa.
 - Para ver más información sobre una escena, haga clic en la escena en la columna de la izquierda y se completarán las columnas **Detalle de la escena** y **Archivos**.
- La columna **Detalle de la escena** (centro) proporciona una descripción más detallada de la escena, incluyendo *Fecha/Hora de inicio*, *Modo de haz*, *Ruta*, *Fotograma*, *Dirección de vuelo*, *Polarización* , *Absolute Orbit* y una imagen de exploración (si está disponible). No todas las escenas tendrán toda la información adicional.
             - El botón **Herramienta de línea de base** abre la herramienta de línea de base ASF, que se utiliza para crear pilas InSAR.
             - El botón **Herramienta SBAS** abre la herramienta ASF SBAS, que es otro método para crear pilas InSAR.
             - El botón **Más como esto** crea una búsqueda basada en la ruta y el fotograma de la escena seleccionada.
              ![tipo:vídeo](https://www.youtube.com/embed/h7vmrcpMd60)
                 - El botón **Cita** abre una nueva ventana con orientación para citar trabajos publicados utilizando datos, imágenes o herramientas a las que se accede a través de ASF.
- **Descargar esta imagen** descarga la imagen de exploración.
             - El icono del ojo con la etiqueta **Abrir en el visor de imágenes** abre una ventana más grande del visor de exploración.
                  - En el visor de exploración, haga **ampliar** usando los botones **+** o **-**. También puede hacer zoom y desplazarse con el mouse.
                   -Haga clic o desplácese por las miniaturas en la parte inferior para ver otras imágenes de exploración de escenas devueltas por su búsqueda.
                   - De forma predeterminada, la casilla **Mostrar solo escenas con una imagen de exploración** está marcada. Puede desmarcar esta opción para ver todas las escenas devueltas por su búsqueda. Las escenas sin una imagen de exploración mostrarán una lista en miniatura *No hay exploración disponible*.
                   - Los metadatos de la escena aparecen en el lado derecho de la ventana del visor de exploración.
          - La columna **Archivos** (derecha) muestra una lista de archivos disponibles para la escena seleccionada actualmente. Puede descargar archivos inmediatamente o agregarlos a su cola de descargas haciendo clic en el icono correspondiente.
         - Al hacer clic en la flecha derecha delante del nombre de un archivo (producto), se expandirá el archivo para mostrar los archivos auxiliares incluidos. Estos archivos pueden descargarse individualmente o agregarse a la cola de descargas.
         - Debes iniciar sesión en Vertex para que esta función funcione.
         - Esta función no está disponible para todos los conjuntos de datos.

## Cola Bajo Demanda

![type:video](https://www.youtube.com/embed/AxhYMBzycuY)

- Al hacer clic en el icono de las **tres cajas** en el encabezado, etiquetado como **Bajo Demanda**, se mostrará una lista desplegable de opciones.
- **Cola Bajo Demanda** abrirá la cola de Bajo Demanda.
    - Los diferentes tipos de trabajos en su cola están separados por pestañas en la parte superior de la cola. Los tipos de trabajos actualmente disponibles son **RTC GAMMA**, **InSAR GAMMA**, y **autoRIFT**. Puede hacer clic en una pestaña para seleccionarla. La pestaña seleccionada se resalta.
    - Para los trabajos **RTC GAMMA** e **InSAR GAMMA**, hay opciones adicionales de procesamiento disponibles. Las opciones que seleccione se aplicarán a todos los archivos de ese tipo de trabajo en su cola.
        - Puede colocar el cursor sobre cada opción para mostrar un mensaje emergente con detalles sobre la opción.
    - Elija su orden de clasificación deseado con las cajas desplegables **Criterio de Orden** y **Orden de Clasificación**.
        - En **Criterio de Orden**, puede elegir ordenar los archivos por *Fecha de Inicio* del archivo o por *Fecha de Agregado* a la cola.
        - En **Orden de Clasificación**, puede elegir ordenar los archivos por el *Más Reciente* o más reciente, o por el *Más Antiguo*.
    - La lista de archivos que ha agregado a su cola se encuentra debajo de las opciones. La X le permite eliminar los archivos que desee de la cola.
    - **Limpiar** mostrará algunas opciones para eliminar archivos de su cola. Puede optar por limpiar una pestaña individual o puede elegir **Limpiar Todos los Tipos de Procesamiento** para eliminar todos los archivos de la cola. Si elige eliminar todos los archivos, se mostrará la opción *Restaurar* para permitirle deshacer esta acción.
    - El número de trabajos restantes se muestra en la parte inferior de la cola. Se asignan 1,000 trabajos a cada usuario por mes. Si tiene demasiados trabajos en su cola, se mostrará un mensaje que indique la cantidad de trabajos adicionales en la parte superior de la cola. El botón **Enviar** estará desactivado.
    - Cuando esté satisfecho con sus selecciones, haga clic en **Enviar Trabajos** en la parte inferior. Esto mostrará la ventana de Revisión de Envío.
        - El campo **Nombre del Proyecto** le permite crear un nombre para los archivos que desea enviar para su procesamiento. El límite de caracteres es 20. Este campo es opcional.
        - Puede seleccionar o deseleccionar las casillas de verificación para enviar solo los tipos de trabajo que desee.
        - Seleccione **Cancelar** para volver a la cola sin enviar ningún archivo para su procesamiento.
        - Haga clic en **Enviar** para enviar sus trabajos. *Nota:* El botón de Envío mostrará la cantidad de trabajos que está enviando.
        - Si hay errores, como falta de cobertura DEM, se mostrará un mensaje de error.
- **Productos Enviados** cambiará al tipo de búsqueda de Productos Bajo Demanda y mostrará sus productos enviados.
- **Documentación de Bajo Demanda (HyP3)** lo llevará a la [documentación de Bajo Demanda](https://hyp3-docs.asf.alaska.edu/)
- *Nota*: Debe iniciar sesión para ver sus Productos Enviados y para enviar trabajos desde la Cola Bajo Demanda.

## Cola de Descargas

![type:video](https://www.youtube.com/embed/cRjqbLNv4Aw)

La funcionalidad mejorada de la cola de descargas ahora está disponible en el navegador Google Chrome. Consulta [a continuación](/vertex/manual/#google-chrome-browser) para obtener más información.

- Al hacer clic en el icono del **carrito de compras** en el encabezado, etiquetado como **Descargas**, se mostrará el contenido de tu cola de descargas actual.
    - Dentro de la cola de descargas, se muestra la lista de archivos que has seleccionado para descargar con información básica de cada archivo, como tipo de archivo y tamaño.
        - Los ID de archivo (nombres) se pueden copiar con el icono de **copiar**.
        - Los archivos se pueden descargar individualmente con el icono de **nube**. También puedes hacer clic derecho para guardar o copiar la URL de descarga.
        - Los elementos se pueden eliminar de la cola con la **X**.
    - **Limpiar** eliminará todos los archivos de la cola. La opción *Restaurar* se mostrará para permitirte deshacer esta acción.
    - **Copiar ID de Archivo** copiará los nombres de archivo de todos los archivos en la cola para usar en otro lugar. Por ejemplo, esta lista podría pegarse en la ventana de *Búsqueda de Lista*.
    - **Copiar URLs** copiará las URL de descarga de todos los archivos en la cola.
    - **Descarga de Datos** se utiliza para descargar varios productos, ya sea con la opción *Descargar Script de Python (.py)* o la opción de archivo *Metalink (metalink)*.
    - **Descarga de Metadatos** se utiliza para exportar el contenido de la cola de descargas a un archivo *CSV*, *KML*, o *GeoJSON*. Los archivos *KML* y *GeoJSON* proporcionados por esta función son compatibles con la función de *Importar Búsqueda Geográfica*.

### Navegador Google Chrome

La funcionalidad mejorada de la cola de descargas está disponible en el navegador Google Chrome. Ten en cuenta que esta funcionalidad mejorada no es compatible cuando se utiliza el modo incógnito.

- Haz clic en el icono del **carrito de compras** en el encabezado, etiquetado como **Descargas** para abrir tu cola de descargas.
    - Junto a cada archivo, puedes hacer clic en el icono de **nube** para comenzar la descarga.
        - A medida que comienza la descarga, un indicador de progreso muestra el porcentaje descargado. Una vez que la descarga se ha completado, el icono aparece como una **marca de verificación** para indicar que el archivo ha sido descargado.
        - Mientras el archivo se está descargando, puedes hacer clic en el indicador de progreso para detener la descarga.
    - En **Descarga de Datos**, puedes seleccionar **Descargar Todo**. Esto descargará 3 archivos a la vez hasta que se hayan descargado todos los productos en tu carrito. Se mostrarán los mismos indicadores de progreso y marcas de verificación para informarte sobre el estado de cada descarga en tu cola.
        - Cuando hagas clic en **Descargar Todo**, aparecerá una ventana de diálogo:
            1. Navega hasta la carpeta donde deseas guardar los archivos y haz clic en *Seleccionar*.
            2. Haz clic en *Ver Archivos* para permitir que la descarga continúe.
            3. Haz clic en *Guardar Cambios* para guardar tus preferencias de carpeta de descarga. Esto persistirá mientras la ventana del navegador Vertex esté abierta.
    - Si **Limpias** los productos de tu cola, los indicadores de progreso y finalización de la descarga se reiniciarán. Puedes volver a agregar los productos a tu cola si lo deseas.
    - *Nota*: Debes iniciar sesión para descargar archivos. Si no has iniciado sesión, al hacer clic para comenzar una descarga, serás redirigido primero a la página de inicio de sesión.

## Otras Opciones de Vertex

En la esquina superior izquierda del mapa, hay botones que te permiten cambiar tu **proyección de mapa**, **zoom**, y **vista de mapa**. *Nota:* Los controles de mapa disponibles varían según el tipo de búsqueda.
![type:video](https://www.youtube.com/embed/qrUnsbZTVnA)
    - Por defecto, el mapa está en proyección ecuatorial. Puedes hacer clic en **Vista de Mapa** y seleccionar **Vista de Mapa Ártico** o **Vista de Mapa Antártico** para cambiar tu proyección de mapa. Haz clic en **Vista de Mapa Ecuatorial** para volver a la proyección ecuatorial.
    - Puedes hacer clic en los iconos de **Aumentar Zoom** o **Reducir Zoom** para ajustar tu nivel de zoom.
    - La capa de mapa predeterminada es satelital. Puedes hacer clic en el botón **Capas** y seleccionar **Vista Satelital** o **Vista de Calle** para cambiar tu capa de mapa.
        - Puedes hacer clic en **Mapa de Visión General** para agregar un mapa de visión general en la esquina superior derecha del mapa. Haz clic nuevamente para desactivar el mapa de visión general.
        - Puedes hacer clic en **Líneas de Cuadrícula** para agregar una superposición de graticule al mapa. Haz clic nuevamente para desactivar la superposición. *Nota*: Actualmente, esto solo está disponible en la vista de mapa ecuatorial.
    - Puedes hacer clic en **Opacidad** y ajustar el control deslizante según desees para cambiar la opacidad de las imágenes de vista previa mostradas en el mapa.
- Haz clic en la **flecha hacia abajo** en la **Búsqueda**
    - **Limpiar Búsqueda** eliminará todos los parámetros de búsqueda que se hayan establecido, excepto el Tipo de Búsqueda y el Conjunto de Datos.
    - **Búsquedas Guardadas** abre un submenú.
    ![type:video](https://www.youtube.com/embed/io4OQumWrJA)
        - **Guardar Búsqueda^** te permite nombrar y guardar tu búsqueda actual.
        - **Ver Búsquedas...^** abre una lista de búsquedas que has nombrado y guardado. Haz clic en el icono de lupa para cargar los ajustes de búsqueda.
        - **Historial de Búsqueda...^** abre una lista de tus 10 últimas búsquedas que no fueron nombradas ni guardadas. Haz clic en el icono de lupa para cargar los ajustes de búsqueda.
    - **Filtros Guardados** abre un submenú.
        - **Guardar Filtros^** te permite guardar tu conjunto actual de filtros.
        - **Ver Filtros...^** te permite ver tus conjuntos de filtros guardados. Haz clic en Aplicar Filtros para aplicarlos a tu búsqueda actual.
    - **Compartir Búsqueda** abre un submenú.
        - **Copiar Enlace de Búsqueda** copiará todos los parámetros de búsqueda que se hayan establecido en la búsqueda actual como una URL. Luego, la URL se puede pegar en la barra de búsqueda del navegador para recrear la búsqueda exactamente, o pegar en un documento y guardarla para recrear la búsqueda más tarde.
        - **Compartir por Correo Electrónico** abrirá un nuevo correo electrónico con la URL de la búsqueda para enviar a otras personas.
    - **Ayuda y Tutoriales** proporciona demostraciones tanto ilustradas como en video de los pasos básicos para configurar una búsqueda y ver los resultados.
        - ^*Nota*: Debes estar registrado en Vertex para que estas opciones estén disponibles.
    - **Exportar** abre un submenú.
        - **Exportar Python** proporcionará un fragmento de código en Python para recrear la búsqueda actual utilizando el módulo de búsqueda Python asf_search. También proporciona un enlace a la documentación de asf_search.
        - **Exportar API** proporcionará la URL de la API para recrear la búsqueda actual utilizando SearchAPI. También proporciona un enlace a la documentación de SearchAPI.

- Haz clic en **Ayuda** para ver opciones adicionales de ayuda.
    - **Ver Nuestros Tutoriales** proporciona demostraciones tanto ilustradas como en video sobre cómo usar Vertex.
    - **Leer Nuestra Guía de Usuario** abre la documentación de Vertex en una nueva pestaña.
    - **Leer Nuestra Guía Bajo Demanda** abre la documentación de Bajo Demanda en una nueva pestaña.
    - **Encontrar Datos SAR Usando la API de ASF** abre la documentación de SearchAPI en una nueva pestaña.
    - **Obtener Más Información Sobre ASF y SAR** abre el sitio web de ASF en una nueva pestaña.
    - **Estadísticas y Repositorio en GitHub** proporciona enlaces a nuestro repositorio de GitHub de Vertex.
- Haz clic en el icono de **Iniciar Sesión** una vez que hayas iniciado sesión para mostrar las opciones de usuario.
    - **Búsquedas Guardadas** abre una lista de búsquedas que has nombrado y guardado. Haz clic en el icono de lupa para cargar la configuración de búsqueda.
    - **Historial de Búsqueda** abre una lista de tus últimas 10 búsquedas que no fueron nombradas ni guardadas. Haz clic en el icono de lupa para cargar la configuración de búsqueda.
    - **Filtros Guardados** abre una lista de filtros que has guardado. Haz clic en *Aplicar Filtros* para aplicar el conjunto de filtros seleccionado a tu búsqueda.
    - **Preferencias** abre una ventana que te permite configurar las preferencias de búsqueda para el idioma, el tema, el conjunto de datos, el número máximo de resultados, la capa de mapa y los ajustes de filtro predeterminados. Estas preferencias se guardarán y se aplicarán a futuras búsquedas.
- *Nota*: **Búsquedas Guardadas**, **Filtros Guardados** y **Historial de Búsqueda** están disponibles tanto a través del menú de Iniciar Sesión como del menú desplegable de la flecha hacia abajo de Búsqueda.
- Haz clic en el campo **Buscar en todo ASF** en la barra de encabezado gris para realizar una búsqueda. Los datos introducidos en este campo buscarán en todos los sitios web de ASF.
    - También puedes hacer clic en el icono de **micrófono** si prefieres usar la búsqueda por voz.
    - A medida que escribas o hables, los resultados de tu búsqueda se mostrarán en una lista debajo del campo. Hacer clic en un resultado de la lista abrirá una nueva pestaña del navegador.
    - Puedes hacer clic en el icono de **lupa** para expandir los resultados de búsqueda. Esto se abrirá en la misma ventana del navegador. Para cerrar y volver a Vertex, haz clic en la **X** cerca de la parte superior derecha de tu pantalla.



# Tipo de búsqueda de referencia

## ¿Qué es la línea base?
La línea de base utiliza información de dos imágenes de radar de apertura sintética (SAR) de la misma área objetivo adquiridas en diferentes momentos (línea de base temporal) y desde posiciones de órbita de satélite ligeramente diferentes (línea de base perpendicular). La herramienta de línea base Vertex te ayuda a identificar y seleccionar pares de escenas que sean apropiados para el procesamiento de SAR interferométrico (InSAR). Proporciona visualización de datos de línea base perpendiculares y temporales y te permite cambiar fácilmente la escena de referencia utilizada en cualquier pila.

## Cómo usar la herramienta Vertex Baseline
Visita ** [ASF's Vertex] (https://search.asf.alaska.edu) ** para comenzar a usar la herramienta Baseline.
! [Tipo: vídeo] (https://www.youtube.com/embed/Xp5bgvi2pEM)

### ** Comenzando tu búsqueda inicial **

- Si no has elegido una escena de referencia en particular, puedes buscar escenas utilizando la búsqueda geográfica o por lista. La columna central tendrá un botón debajo de los metadatos titulado *** Herramienta de línea de base *** para cualquier escena que sea elegible. Puedes hacer clic en este botón para ser dirigido a una búsqueda de referencia. La búsqueda de línea base usará la escena elegida como escena de referencia.

- Si has elegido una escena de referencia en particular, puedes seleccionar ***Línea de base*** en la lista desplegable Tipo de búsqueda. Puedes ingresar tu escena de referencia y presionar ***Buscar***.

### **Interactuar con los resultados de búsqueda de referencia**
Mientras estés en el tipo de búsqueda de referencia, notarás muchos controles familiares en el panel de resultados. Las escenas aparecen en la columna de la izquierda. Las líneas de base perpendiculares y temporales se enumeran al lado de cada escena. La columna central enumera los metadatos de la escena seleccionada e incluye el botón **Establecer como referencia**, que te permite configurar cualquier escena de la pila como escena de referencia. El gráfico de referencia aparece en la columna de la derecha.

**Controles del panel de resultados**

- En la parte superior izquierda del panel de resultados, verás la cantidad de escenas enumeradas.
- **Zoom** hará *Acercar los resultados* ampliando el área del mapa de la Tierra donde se encuentran las escenas.
- **Cola*** Agregará todos los resultados a Descargas*permitiéndote agregar todas las escenas a la cola de descargas.
- **On Demand** te permitirá *Agregar todos los resultados a la cola On Demand* para realizar un procesamiento personalizado en las escenas. Para obtener más información, haz clic [aquí] (https://hyp3-docs.asf.alaska.edu/using/vertex/). También puedes optar por *Crear suscripción *. Puedes encontrar más detalles sobre las suscripciones [aquí] (https://hyp3-docs.asf.alaska.edu/using/subsitas/).
- **Exportar** te permitirá*Descargar datos/metadatos*para todas las escenas de la pila.
- En la columna de la izquierda, **Cola** *Agregarás archivos de escena a las descargas* solo para la escena seleccionada.
- Debajo de los metadatos en la columna central, ** Establecer como referencia ** te permitirá establecer cualquier escena en la pila como escena de referencia. Cuando selecciones esto, tanto el gráfico como los valores de referencia se actualizarán automáticamente.

** Controles de gráficos **

- Los puntos en el gráfico representan escenas individuales. Al pasar el cursor sobre ellos, se enumerarán sus valores temporales y perpendiculares. También puedes hacer clic en cualquier punto para seleccionar esa escena. Se actualizarán los metadatos de la columna central.
- Ubicado encima del gráfico, encontrarás las etiquetas y los colores correspondientes. Estos indican cómo se muestran en el gráfico la escena de referencia, la escena seleccionada y cualquier escena en su cola de descarga. Algunos conjuntos de datos incluyen un área sombreada que indica la línea de base crítica.
- Puedes ampliar y desplazar el gráfico.

#### Criterios de referencia

- Puedes hacer clic en ** Criterios de referencia ... ** encima del gráfico para ver opciones adicionales.
- Puedes ajustar los controles deslizantes para cambiar los valores perpendiculares y temporales que deseas incluir en tus resultados.
- Puedes ingresar una fecha de inicio y finalización.
- Cambiar cualquier criterio actualizará automáticamente la lista de escenas y el gráfico.

## Próximos pasos
Una vez que estés satisfecho con tu conjunto de resultados, puedes usar la cola de descarga para administrar y descargar los resultados de referencia. Puedes encontrar más información sobre la cola de descarga en la [Guía del usuario de introducción a Vertex] (/vertex/manual).

Si quieres crear interferogramas, el procesamiento personalizado ahora está disponible a través de Vertex. Los detalles están disponibles en la sección Cola On Demand de la [Guía del usuario de introducción a Vertex] (/vertex/manual). Puedes encontrar más información sobre la creación de interferogramas con el procesamiento personalizado de ASF a través de la [documentación de HyP3] (https://hyp3.asf.alaska.edu/about).
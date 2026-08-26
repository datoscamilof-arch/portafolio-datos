# Análisis Comercial y Segmentación de Clientes (Modelo RFM) - Interforros

## Contexto

Este proyecto aplica técnicas de análisis de datos y modelado RFM (Recencia, Frecuencia, Monto) para un negocio de retail especializado en accesorios automotrices (Interforros). El objetivo es transformar registros transaccionales crudos en insights accionables, aplicando principios de Data Storytelling para facilitar la toma de decisiones gerenciales.

## Pregunta de Negocio

* ¿Qué categorías de productos y canales de venta impulsan la mayor rentabilidad del negocio?
* ¿Cómo se distribuye la cartera de clientes según su comportamiento histórico de compra, lealtad y riesgo de abandono?
* ¿Qué acciones estratégicas inmediatas deben implementarse para maximizar la retención y proteger el capital estancado?

## Herramientas Utilizadas

* Python (Pandas): Análisis Exploratorio de Datos (EDA), limpieza de la base transaccional y cálculo algorítmico de los scores RFM.
* Power BI: Modelado relacional, creación de medidas dinámicas (DAX) y diseño del dashboard interactivo.
* Data Storytelling: Aplicación de metodologías de diseño visual (basadas en Cole Nussbaumer Knaflic) orientadas a reducir el ruido visual y destacar hallazgos mediante títulos declarativos.

## Estructura del Proyecto

03-Interforros-rendimiento-rfm/
├── README.md
├── ventas_retail.csv             # Dataset crudo original con transacciones
├── 01_Limpieza_y_RFM.py          # Script de Python para limpieza y cálculo RFM
├── ventas_limpias.csv            # Dataset procesado, libre de atípicos y errores
├── rfm_clientes_limpio.csv       # Tabla dimensional de clientes segmentados
├── Interforros.pbix              # Dashboard interactivo en Power BI
└── img/
    ├── Rendimiento.png           # Captura de la página 1
    └── RFM.png                   # Captura de la página 2

## Estructura del Dashboard

[Ver dashboard interactivo en Power BI](https://app.powerbi.com/view?r=eyJrIjoiZWIwNzYwY2EtNWYzYS00YWM1LTlmNzItMTFlMDM3MjEwY2UzIiwidCI6ImZkNzY2ZWRkLThiZWEtNGM5OS04NjcyLTU2ZDFjYWJjMjcwNiIsImMiOjR9)

**Página 1: Resumen Ejecutivo (Rendimiento Comercial)**
Diseñada para evaluar de un vistazo el volumen total de ventas. Permite identificar la dependencia financiera por categoría de producto, la distribución de ingresos por canal y la tendencia o estacionalidad mensual de la facturación.

![Página 1 - Rendimiento Comercial](img/Rendimiento.png)

**Página 2: Diagnóstico de Cartera (Segmentación RFM)**
Diseñada para el equipo comercial y estratégico. Analiza la composición de los clientes mediante una matriz de calor (Recencia vs. Frecuencia) y clasifica la base en cinco segmentos clave, asociando el ingreso histórico retenido con recomendaciones tácticas directas.

![Página 2 - Segmentación RFM](img/RFM.png)

## Principales Hallazgos

* Dominio de categoría: Los Forros de Asiento son el motor financiero indiscutible del negocio, concentrando el 64,57% de los ingresos totales ($108 millones).
* Dependencia del canal físico: La tienda física representa el 61,6% de la facturación, evidenciando un rezago en la adopción de canales digitales (Web concentra apenas el 10,19%).
* Capital crítico en riesgo: El 24% del ingreso ($40,4 millones) depende de clientes clasificados analíticamente como "En Riesgo".
* Fuga de clientes: Los segmentos "Perdidos" y "En Riesgo" suman en conjunto el 49% de la base de clientes (147 de 298), confirmando que el reto principal del negocio es la retención, dado que el ticket promedio no muestra variaciones drásticas entre grupos.
* Estacionalidad operativa: Se identificó una caída crítica de demanda en el mes de abril, seguida inmediatamente por un pico histórico de ventas en mayo ($17 millones).

## Próximos Pasos

* Ejecutar una campaña de reactivación urgente y selectiva enfocada exclusivamente en los 72 clientes del segmento "En Riesgo" para proteger los $40,4 millones comprometidos.
* Diseñar estrategias de incentivo (descuentos cruzados o envíos gratuitos) para traccionar el volumen de la tienda física hacia los canales Web y WhatsApp.
* Ajustar la planeación de inventarios preventivos en el primer trimestre para mitigar el impacto del valle de abril y soportar el pico transaccional de mayo.

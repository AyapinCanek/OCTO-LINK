# Fundamentos teóricos y distinciones

## Pregunta principal

¿Puede un agente computacional cumplir objetivos físicos sobre un cuerpo simulado, detectar restricciones y reconocer metas imposibles?

## Por qué partir de un organismo simple

*C. elegans* inspira la idea de estudiar relaciones entre actividad nerviosa, locomoción y objetivos. El modelo aquí construido es **un agente de cuadrícula**, no un modelo de sus 302 neuronas, músculos, estados bioquímicos ni conectoma. La correspondencia biológica queda como trabajo futuro de revisión bibliográfica, no como resultado demostrado.

## Conceptos operacionales

- **Observación:** estimar posición y entorno a partir de sensores.
- **Predicción:** anticipar el resultado de una acción.
- **Planificación:** seleccionar pasos hacia una meta con restricciones.
- **Control:** aplicar acciones a un cuerpo simulado y comprobar su evolución.
- **Imposibilidad:** demostrar que no existe ruta bajo las reglas actuales del mapa, no declarar imposible una misión en todo contexto físico.

## Restricciones del experimento

Un mapa finito contiene casillas libres y barreras rígidas infranqueables. Los movimientos válidos son norte, sur, este y oeste. No se permite atravesar paredes, teletransportarse ni desplazar obstáculos. BFS puede verificar exhaustivamente si existe ruta.

## Qué sería evidencia de progreso

A diferencia del planificador de referencia, un agente con observación parcial debe explorar, actualizar su mapa y decidir cuándo carece de evidencia suficiente. Los resultados se evaluarán con métricas de éxito, colisiones, longitud de trayectoria, recursos utilizados y precisión al reportar imposibilidad.

## Límites

Ningún resultado del simulador demuestra que sea posible imponer órdenes a un animal real, leer su mente o conectar un casco a un cerebro. Cualquier extrapolación entre simulación y biología necesita investigación independiente y supervisión ética.

# OCTO-LINK 🐙

**Investigación abierta de IA corporizada, convivencia responsable y control de cuerpos virtuales.**

**Autor y fundador del proyecto:** AyapinCanek  
**Asistencia técnica y documentación inicial:** ChatGPT (GPT-6, asistente de IA de OpenAI)  
**Inicio:** 7 de noviembre de 2026  
**Versión:** 0.2.0 — prototipos conceptuales, sin validación clínica, biológica ni social.

> Este proyecto **no** pretende controlar personas ni intervenir animales vivos. La primera etapa consiste exclusivamente en simulaciones informáticas. El reconocimiento de límites físicos y la seguridad son requisitos de diseño.

## Visión

La prioridad definida por AyapinCanek es investigar una **IA capaz de convivir físicamente**, mediante un cuerpo artificial que perciba y actúe con límites seguros, para ayudar a prevenir daños evitables y apoyar la convivencia humana. El pulpo es una inspiración histórica del diálogo, **no un requisito de diseño**. La fase actual es solo simulación y **no demuestra beneficio psicológico o social**. Véase [`docs/VISION_CONVIVENCIA.md`](docs/VISION_CONVIVENCIA.md).


Investigar cómo un sistema de IA puede recibir una misión, percibir restricciones físicas, planificar movimientos, detectar imposibilidades y coordinar un cuerpo *virtual*. La inspiración a largo plazo es un robot blando con ocho brazos semejante a un pulpo. Se parte de un agente sencillo, inspirado de forma conceptual en el tamaño y la locomoción de *C. elegans*, **sin afirmar que simule fielmente sus neuronas**.

## Hipótesis inicial

Un controlador digital con información del entorno puede distinguir entre un objetivo alcanzable y uno bloqueado, proponer una trayectoria y documentar el resultado. Esta hipótesis se evalúa en un entorno cuadriculado; no prueba control neuronal de un organismo.

## Primeros experimentos

1. **Salida:** encontrar una ruta a través de un laberinto.
2. **Barrera:** encontrar una ruta alternativa cuando el camino directo está obstruido.
3. **Imposibilidad:** reconocer que el objetivo está completamente aislado y reportar que no existe una ruta.

Los experimentos iniciales usan búsqueda en anchura (BFS) como referencia verificable; **todavía no incorporan una IA neuronal ni un cerebro biológico**. Son un punto de partida para comparar controladores posteriores.

## Ejecutar

Requisitos: Python 3.10 o superior, sin dependencias externas.

```bash
python3 -m src.simulator
python3 -m src.convivencia
python3 -m unittest discover -s tests -v
```

## Estructura

- `src/simulator.py`: misiones, mapa y controlador de referencia.
- `src/convivencia.py`: simulador inicial de consentimiento y acciones permitidas.
- `tests/test_simulator.py`: pruebas de éxito, restricciones e imposibilidad.
- `tests/test_convivencia.py`: pruebas de consentimiento, rechazo y retirada.
- `docs/VISION_CONVIVENCIA.md`: visión, principios, métricas e hitos de convivencia.
- `docs/TEORIA.md`: preguntas y límites científicos.
- `docs/HOJA_DE_RUTA.md`: etapas y criterios de avance.
- `docs/AUTORES.md`: crédito y contribuciones.
- `CONTRIBUTING.md`: instrucciones para personas y agentes de IA.
- `AGENTS.md`: tareas y reglas reproducibles para asistentes automatizados.
- `LICENSE`: licencia MIT.

## Participación abierta

Se aceptan propuestas, issues, pruebas, modelos simulados y pull requests. Publicarlo en GitHub **no hace que todas las IA trabajen automáticamente en él**: los agentes y sus responsables deben elegir participar y contar con acceso autorizado.

## Seguridad y alcance

No se desarrollarán protocolos para someter animales, implantar dispositivos o estimular sistemas nerviosos vivos. La investigación experimental con seres vivos requiere supervisión veterinaria, revisión ética y cumplimiento normativo. El desarrollo práctico de este repositorio se limita a software, simulación y robótica no biológica.

## Estado

Prototipo documentado y ejecutable. Aún no publicado en GitHub hasta que la persona propietaria autorice la conexión o realice la subida.

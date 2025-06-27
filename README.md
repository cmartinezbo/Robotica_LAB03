<div align="center">
<picture>
    <source srcset="https://imgur.com/5bYAzsb.png" media="(prefers-color-scheme: dark)">
    <source srcset="https://imgur.com/Os03JoE.png" media="(prefers-color-scheme: light)">
    <img src="https://imgur.com/Os03JoE.png" alt="Escudo UNAL" width="350px">
</picture>

<h3>Curso de Robótica 2025-I</h3>

<h1>Laboratorio 03</h1>

<h2>Robótica Industrial - Análisis y Operación del
Manipulador Motoman MH6</h2>

<h4>Juan José Díaz Guerrero<br>
    Cristian Fabián Martínez Bohórquez</h4>

</div>

<div align="justify"> 

## Análisis Comparativo: Robots Industriales Motoman MH6 vs ABB IRB 140

| Característica               | **Motoman MH6**                                   | **ABB IRB 140**                                    |
|------------------------------|--------------------------------------------------|--------------------------------------------------|
| **Fabricante**               | Yaskawa Electric Corporation                    | ABB                                              |
| **Capacidad de carga**       | 6 kg                                            | 6 kg                                             |
| **Radio de trabajo**         | 1373 mm                                         | 810 mm                                           |
| **Grados de libertad**       | 8                                               | 6                                               |
| **Repetibilidad**            | ±0.08 mm                                        | ±0.03 mm                                         |
| **Velocidades máximas**      | - Eje S: 170°/s                                | - Eje S: 250°/s                                |
|                              | - Eje L: 140°/s                                | - Eje L: 250°/s                                |
|                              | - Eje U: 160°/s                                | - Eje U: 300°/s                                |
|                              | - Eje R: 400°/s                                | - Eje R: 320°/s                                |
|                              | - Eje B: 430°/s                                | - Eje B: 410°/s                                |
|                              | - Eje T: 700°/s                                | - Eje T: 500°/s                                |
| **Masa del robot**           | 130 kg                                          | 98 kg                                            |
| **Campos de aplicación**     | Soldadura, manejo de materiales, ensamble      | Ensamble, empaquetado, manipulación, paletizado |
| **Protección ambiental**     | IP54 (estándar), IP65 para brazo (opcional)     | IP67 (estándar)                                 |
| **Sistema de control**       | DX100, DX200, FS100                             | IRC5 Compact                                    |
| **Alimentación eléctrica**   | 3 fases, 380-480 V                              | 3 fases, 200-600 V                              |
| **Opciones de montaje**      | Suelo, techo, pared                             | Suelo, pared, techo, invertido                  |
| **Costo aproximado**         | Alrededor de $35,000 USD                        | Alrededor de $25,000 USD                        |

## Configuraciones Home1 y Home2 del Motoman MH6

El manipulador Motoman MH6 cuenta con dos posiciones de referencia predefinidas denominadas **Home1** y **Home2**. Estas configuraciones sirven como puntos de partida seguros para el robot y facilitan las operaciones de calibración y posicionamiento inicial.

Las diferencias principales entre estas posiciones radican en:

- **Orientación de las articulaciones**: Cada configuración establece ángulos específicos para optimizar diferentes tipos de operaciones
- **Accesibilidad del espacio de trabajo**: Dependiendo de la aplicación, una configuración puede proporcionar mejor acceso a ciertas áreas
- **Consideraciones de seguridad**: Ambas posiciones están diseñadas para minimizar riesgos durante el arranque del sistema

La selección entre Home1 y Home2 depende de los requerimientos específicos de la tarea y la configuración de la celda robotizada.

## Operación Manual del Robot

### Control por Articulaciones Individuales
1. **Activación del modo de enseñanza**:
   - Presionar el botón `TEACH` en el pendant de programación para habilitar el control manual
   - Configurar el selector en "Joint Mode" para acceder al control articular

2. **Selección de la articulación**:
   - Navegar en la pantalla para elegir la articulación específica (J1 hasta J6)

3. **Ejecución del movimiento**:
   - Utilizar las teclas direccionales (`+` o `-`) para generar movimiento en sentido horario o antihorario de la articulación seleccionada

### Transición a Control Cartesiano
1. **Cambio de modalidad**:
   - Modificar la configuración del Teach Pendant al "Cartesian Mode"

2. **Selección del eje de movimiento**:
   - Especificar en pantalla el eje cartesiano deseado (X, Y, Z)

3. **Ejecución de movimientos lineales**:
   - Emplear las teclas direccionales (`+` o `-`) para desplazar el efector final en la dirección del eje elegido

### Control de Orientación (Movimientos Rotacionales)
1. **Selección del eje rotacional**:
   - En modo cartesiano, especificar el eje de rotación requerido (Rz, Ry, Rx)

2. **Ejecución de la rotación**:
   - Aplicar las teclas direccionales (`+` o `-`) para rotar el efector final alrededor del eje seleccionado

## Gestión de Velocidades en Operación Manual

El sistema de control del Motoman MH6 incorpora múltiples niveles de velocidad para optimizar la precisión y eficiencia durante los movimientos manuales:

1. **Configuración de velocidades**:
   - El rango abarca desde configuraciones "Low" (baja) hasta "High" (alta), incluyendo opciones intermedias como "Medium"
   - La configuración se realiza mediante el potenciómetro de velocidad del Teach Pendant o a través de los menús en pantalla

2. **Modificación dinámica de velocidad**:
   - El potenciómetro permite ajustes en tiempo real durante la operación
   - Como alternativa, el botón `SPEED` del colgante proporciona acceso directo al menú de selección de velocidades

3. **Visualización del estado actual**:
   - El nivel de velocidad activo se presenta en la esquina superior derecha de la pantalla del Teach Pendant
   - La información se muestra como porcentaje (25%, 50%, 100%) o mediante etiquetas descriptivas (Low, Medium, High)

## RoboDK: Capacidades y Comunicación con Manipuladores

### Funcionalidades Principales de RoboDK
RoboDK constituye una plataforma integral de simulación y programación offline diseñada para robots industriales, destacando por:

1. **Modelado de Celdas Robotizadas**:
   - Facilita el diseño y validación de sistemas robotizados completos previo a su implementación física
   - Optimiza la verificación de alcances, detección de colisiones y aprovechamiento del espacio de trabajo

2. **Programación Fuera de Línea (OLP)**:
   - Genera código de programación nativo para diversos fabricantes de robots sin requerir programación directa en el controlador
   - Minimiza significativamente los tiempos de inactividad del equipo

3. **Conectividad CAD/CAM**:
   - Importa trayectorias y geometrías desde sistemas CAD/CAM para ejecutar aplicaciones especializadas como mecanizado, corte láser o soldadura

4. **Refinamiento de Trayectorias**:
   - Permite la optimización de rutas para maximizar eficiencia operativa y eliminar movimientos redundantes o peligrosos

5. **Ambiente de Formación**:
   - Proporciona un entorno simulado y seguro ideal para la enseñanza de conceptos robóticos y técnicas de programación

### Protocolo de Comunicación RoboDK-Manipulador
La integración entre RoboDK y el manipulador se establece mediante protocolos especializados que permiten la generación y transferencia de programas compatibles:

#### Procedimiento de Control del Manipulador:
1. **Establecimiento de Conexión**:
   - RoboDK se conecta con controladores compatibles (DX100/DX200 para Motoman MH6) utilizando interfaces Ethernet o protocolos específicos del fabricante

2. **Compilación de Código**:
   - El software traduce la simulación configurada en código nativo (formato JBI para Yaskawa Motoman)
   - Este código se transfiere directamente al sistema de control del robot

3. **Implementación en el Robot**:
   - Una vez cargadas las instrucciones, el controlador ejecuta las secuencias programadas siguiendo las trayectorias simuladas

4. **Supervisión en Tiempo Real**:
   - RoboDK ofrece capacidades de monitoreo continuo cuando la conexión permanece activa, garantizando la precisión de las trayectorias ejecutadas

#### Procesos Internos de RoboDK:
- **Conversión de Trayectorias**:
   - Transforma rutas definidas en el entorno virtual en instrucciones específicas interpretables por el controlador

- **Optimización de Secuencias**:
   - Elimina movimientos innecesarios y optimiza trayectorias para mejorar la eficiencia operacional

- **Validación de Seguridad**:
   - Verifica que todas las trayectorias generadas estén libres de colisiones antes del envío al robot físico

La implementación de RoboDK reduce considerablemente los tiempos de programación directa en el controlador mientras asegura movimientos precisos y seguros.

## Análisis Comparativo: RoboDK vs RobotStudio

### RoboDK - Solución Multiplataforma
RoboDK se presenta como una herramienta versátil de programación y simulación offline con soporte para múltiples fabricantes de robots industriales.

**Fortalezas:**
- Compatibilidad universal con diversas marcas y modelos de robots
- Interfaz intuitiva accesible para usuarios con conocimientos básicos en robótica
- Excelente opción para aplicaciones generales que no demandan integración específica con hardware particular
- Capacidad avanzada para generar trayectorias complejas desde sistemas CAD/CAM

**Aplicaciones Recomendadas:**
- Instalaciones de manufactura que operan robots de diferentes fabricantes
- Desarrollo inicial de simulaciones para celdas robotizadas
- Programas de capacitación en robótica industrial genérica

### RobotStudio - Solución Especializada ABB
RobotStudio representa la herramienta oficial desarrollada por ABB específicamente para la simulación y programación offline de su línea de robots industriales.

**Fortalezas:**
- Integración completa y nativa con controladores y componentes de hardware ABB
- Simulaciones de alta precisión para movimientos y análisis de tiempos de ciclo
- Herramientas especializadas para depuración y optimización de programas específicos de ABB
- Acceso completo a funciones avanzadas del controlador IRC5

**Aplicaciones Recomendadas:**
- Desarrollo avanzado de celdas robotizadas exclusivamente ABB
- Configuración detallada de parámetros específicos del controlador IRC5
- Desarrollo de aplicaciones personalizadas con soporte técnico directo de ABB

### Evaluación Comparativa
**RoboDK** se posiciona como la solución ideal para entornos de manufactura heterogéneos que requieren flexibilidad y compatibilidad con múltiples plataformas robóticas. Su diseño orientado a la usabilidad lo convierte en una excelente herramienta para propósitos educativos y simulaciones preliminares.

**RobotStudio** constituye la elección óptima para proyectos que involucran exclusivamente robots ABB, ofreciendo un nivel superior de detalle, precisión y funcionalidad gracias a su integración nativa con el ecosistema tecnológico de ABB. Su especialización permite explotar al máximo las capacidades avanzadas de los sistemas ABB.

</div>

# Práctica 1. Machine Learning: Predicción Multiclase de Riesgo Cardiovascular en Población Adulta

> **Transcripción** del PDF `Practica_1_Machine_Learning_Cardiovascular.pdf` (curso 26-27), para poder consultarlo desde el repositorio. El documento oficial es el PDF publicado en el Aula Virtual; en caso de duda, manda el PDF.
>
> **Nota del equipo:** el título del apartado 3.2 dice «Mínimo 4 Modelos / 3 Ensambles», pero su texto exige como mínimo 5 algoritmos: 2 modelos base y 3 ensambles.

## 1. Planteamiento del problema

Las enfermedades cardiovasculares continúan siendo una de las mayores amenazas para la salud pública global y una de las principales causas de morbimortalidad a nivel mundial. Para combatir este problema, la detección temprana y la estratificación precisa del nivel de riesgo individual son pilares esenciales que permiten aplicar intervenciones preventivas adaptadas a cada paciente y optimizar la gestión de los recursos en los sistemas de salud.

Conscientes de esta necesidad, el equipo médico e investigador del Hospital Morales Meseguer ha puesto en marcha un proyecto estratégico orientado al desarrollo de herramientas predictivas de vanguardia. La iniciativa nace con el objetivo de ofrecer una solución integral basada en datos clínicos que transforme la evaluación del riesgo cardiovascular en la práctica médica diaria, mejorando directamente el diagnóstico y el seguimiento del paciente. Para ello, el equipo médico pone a disposición de este proyecto una cohorte clínica con 2.254 registros de pacientes y 28 variables sociodemográficas, clínicas, analíticas y de estilo de vida para clasificar a los pacientes en tres niveles de riesgo cardiovascular (Clase 0: Bajo Riesgo, Clase 1: Riesgo Moderado y Clase 2: Alto Riesgo).

## 2. Descripción del dataset y diccionario de variables

El archivo de datos suministrado para este estudio es `enfermedad_cardiovascular.csv`. Consta de 28 atributos: 27 variables de entrada y 1 variable objetivo. A continuación, se detalla la definición técnica y el tipo de dato de cada una de las variables incluidas:

| Variable | Tipo | Definición |
|---|---|---|
| `edad` | Numérico | Edad del paciente expresada en años cumplidos. |
| `presion_sistolica` | Numérico | Presión arterial sistólica medida en reposo (mmHg). |
| `presion_diastolica` | Numérico | Presión arterial diastólica medida en reposo (mmHg). |
| `colesterol_total` | Numérico | Nivel de colesterol total en suero (mg/dL). |
| `colesterol_hdl` | Numérico | Nivel de colesterol de alta densidad o 'colesterol bueno' (mg/dL). |
| `colesterol_ldl` | Numérico | Nivel de colesterol de baja densidad o 'colesterol malo' (mg/dL). |
| `trigliceridos` | Numérico | Concentración sérica de triglicéridos (mg/dL). |
| `glucosa_ayunas` | Numérico | Nivel de glucosa en sangre tras ayuno nocturno (mg/dL). |
| `indice_masa_corporal` | Numérico | Índice de masa corporal calculado como peso/talla² (kg/m²). |
| `frecuencia_cardiaca_reposo` | Numérico | Frecuencia cardíaca medida en reposo (latidos por minuto). |
| `horas_sueno_diarias` | Numérico | Promedio de horas de descanso nocturno declaradas por día. |
| `consumo_alcohol_semanal` | Numérico | Unidades de bebida estándar de alcohol consumidas semanalmente. |
| `anos_fumador` | Numérico | Tiempo acumulado de exposición al tabaco expresado en años. |
| `proteina_c_reactiva` | Numérico | Concentración de proteína C reactiva ultrasensible (mg/L). |
| `acido_urico` | Numérico | Nivel sérico de ácido úrico (mg/dL). |
| `clearance_creatinina` | Numérico | Tasa de filtrado glomerular / depuración de creatinina (mL/min). |
| `frecuencia_ejercicio_semanal` | Numérico | Días a la semana con actividad física moderada o intensa. |
| `perimetro_cintura` | Numérico | Circunferencia abdominal medida en centímetros. |
| `hemoglobina_glicosilada` | Numérico | Porcentaje de hemoglobina glicosilada HbA1c en sangre (%). |
| `fumador_actual` | Booleano | Indica el hábito tabáquico activo (1: Sí, 0: No). |
| `hipertension_previa` | Booleano | Diagnóstico previo confirmado de hipertensión arterial (1: Sí, 0: No). |
| `diabetes_mellitus` | Booleano | Diagnóstico previo de diabetes mellitus tipo 2 (1: Sí, 0: No). |
| `tratamiento_estatinas` | Booleano | Uso habitual de fármacos hipolipemiantes / estatinas (1: Sí, 0: No). |
| `uso_antihipertensivos` | Booleano | Uso habitual de medicamentos para el control presivo (1: Sí, 0: No). |
| `tipo_alimentacion` | Nominal | Patrón dietético principal del paciente. Valores posibles: 'Mediterránea', 'Occidental', 'Vegetariana', 'Baja en carbohidratos'. |
| `nivel_actividad` | Nominal | Grado habitual de actividad física diaria. Valores posibles: 'Sedentario', 'Ligeramente activo', 'Moderadamente activo', 'Muy activo'. |
| `antecedentes_familiares_tipo` | Nominal | Presencia de eventos cardiovasculares en familiares de primer grado. Valores posibles: 'Ninguno', 'Materno', 'Paterno', 'Ambos'. |
| `riesgo_cardiovascular` | Objetivo | Variable target de clasificación en 3 categorías (0: Bajo riesgo, 1: Riesgo moderado, 2: Alto riesgo). |

## 3. Tareas y requisitos obligatorios

El trabajo debe cubrir rigurosamente las fases del proyecto. El equipo evaluador requerirá la resolución detallada de los siguientes apartados:

### 3.1. Análisis Exploratorio de Datos e Identificación de Problemáticas

El alumnado deberá realizar un análisis exploratorio exhaustivo del conjunto de datos para auditar su calidad e identificar todas las limitaciones o problemáticas presentes en las variables. Se requiere obligatoriamente:

- Análisis explícito e identificación de las problemáticas presentes en el dataset.
- Propuesta y aplicación de como mínimo tres soluciones o técnicas de preprocesamiento diseñadas específicamente para mitigar y resolver la/s problemática/s detectada/s. Se deben indicar la/s problemática/s detectada/s y explicar la metodología que se seguirá.

### 3.2. Diseño y Entrenamiento de Modelos (Mínimo 4 Modelos / 3 Ensambles)

Se exige el entrenamiento y ajuste comparativo de un panel de como mínimo 5 algoritmos de clasificación donde se requiere obligatoriamente:

- **Modelo Base** (como mínimo, 2 modelos obligatorios): un clasificador básico o lineal.
- **Modelos de Ensamble** (como mínimo 3 modelos obligatorios): tres algoritmos basados en técnicas de ensamble de aprendizaje.

### 3.3. Estrategia de Evaluación y Métricas de Rendimiento

Para garantizar la validez científica y evitar el sobreajuste (overfitting), el alumnado deberá establecer un esquema de validación sólido, capaz de evaluar todas las combinaciones posibles entre los modelos de entrenamiento y las técnicas de preprocesamiento, a fin de abordar las diferentes problemáticas encontradas. Así se requiere:

- **Esquemas de Validación:** Establecer un esquema riguroso, justificar la partición de los datos utilizada y analizar los resultados.
- **Métricas de Evaluación (Mínimo 3 métricas):** Evaluar los modelos utilizando al menos 3 métricas de rendimiento. Se debe razonar, analítica y clínicamente, qué métrica es la más crítica para la toma de decisiones sanitarias y justificar por qué.
- **Ajuste de hiperparámetros:** Todos los modelos deben incluir un ajuste de hiperparámetros que justifique su elección.

### 3.4. Conclusiones

Se deberán obtener conclusiones claras, justificadas y razonadas sobre el mejor modelo de predicción. Este análisis podrá realizarse desde diferentes puntos de vista, siempre y cuando todos estén justificados en relación con el problema planteado. En estas conclusiones, sería interesante realizar una valoración tanto cualitativa como cuantitativa de los mejores modelos seleccionados, analizando aspectos como la complejidad, la interpretabilidad y/o la robustez.

### 3.5. OPCIONAL. Test estadísticos

Este apartado es opcional y se valorará positivamente. Se trata de un trabajo de investigación para comparar estadísticamente, una vez obtenidos todos los modelos, cuál es el mejor modelo centrado en una de las métricas. Para ello, se podría realizar una valoración estadística tanto entre pares de modelos como entre todos ellos.

# Regresión Logística y Entropía Cruzada

## ¿Qué es la regresión logística?

La regresión logística es una técnica de clasificación que se utiliza para predecir la probabilidad de que una observación pertenezca a una de dos clases posibles. Por ejemplo, puede predecir si un correo electrónico es spam o no spam, si un paciente tiene una enfermedad o no, etc.

## ¿Cómo funciona?

### Entrada de datos

Imagina que tienes un conjunto de datos con varias características (por ejemplo, la longitud y el ancho de los pétalos de una flor) y una etiqueta que indica la clase (por ejemplo, si la flor es de la especie A o B).

### Modelo lineal

La regresión logística toma una combinación lineal de las características de entrada. Esto significa que multiplica cada característica por un coeficiente y suma los resultados. Por ejemplo:



\[ z = b_0 + b_1 \cdot x_1 + b_2 \cdot x_2 \]



Donde \( b_0 \) es el término de intersección, \( b_1 \) y \( b_2 \) son los coeficientes, y \( x_1 \) y \( x_2 \) son las características.

### Función sigmoide

Luego, aplica la función sigmoide a esta combinación lineal para obtener una probabilidad entre 0 y 1:



\[ \sigma(z) = \frac{1}{1 + e^{-z}} \]



La función sigmoide transforma cualquier valor en un número entre 0 y 1, que se puede interpretar como una probabilidad.

### Clasificación

Basado en esta probabilidad, el modelo decide a qué clase pertenece la observación. Por ejemplo, si la probabilidad es mayor que 0.5, el modelo clasifica la observación como clase 1; de lo contrario, la clasifica como clase 0.

## Ejemplo práctico

Imagina que estás tratando de predecir si un estudiante aprobará un examen basado en las horas de estudio y la cantidad de sueño que tuvo la noche anterior. Aquí tienes un ejemplo de cómo se vería el proceso:

### Datos de entrada

- Horas de estudio: 5
- Horas de sueño: 7
- Resultado del examen: Aprobado (1) o No aprobado (0)

### Modelo lineal



\[ z = b_0 + b_1 \cdot (\text{Horas de estudio}) + b_2 \cdot (\text{Horas de sueño}) \]



Supongamos que \( b_0 = -1 \), \( b_1 = 0.5 \), y \( b_2 = 0.3 \).

### Cálculo



\[ z = -1 + 0.5 \cdot 5 + 0.3 \cdot 7 = -1 + 2.5 + 2.1 = 3.6 \]



### Función sigmoide



\[ \sigma(3.6) = \frac{1}{1 + e^{-3.6}} \approx 0.974 \]



### Clasificación

- Probabilidad de aprobar: 0.974 (97.4%)
- Como 0.974 > 0.5, el modelo predice que el estudiante aprobará el examen.

## ¿De dónde vienen los coeficientes?

### Datos de entrenamiento

Primero, necesitas un conjunto de datos de entrenamiento que contenga ejemplos de las características (por ejemplo, horas de estudio y horas de sueño) y las etiquetas correspondientes (por ejemplo, si el estudiante aprobó o no).

### Entrenamiento del modelo

Durante el entrenamiento, el modelo de regresión logística ajusta los coeficientes \( b_0 \), \( b_1 \) y \( b_2 \) para minimizar la diferencia entre las predicciones del modelo y las etiquetas reales en el conjunto de datos de entrenamiento. Este proceso se llama optimización.

### Función de costo

El modelo utiliza una función de costo (como la entropía cruzada) para medir qué tan bien está haciendo las predicciones. La optimización ajusta los coeficientes para minimizar esta función de costo.

### Algoritmo de optimización

Un algoritmo comúnmente utilizado para ajustar los coeficientes es el gradiente descendente, que iterativamente ajusta los coeficientes en la dirección que reduce la función de costo.

## Ejemplo práctico

Imagina que tienes un conjunto de datos con las siguientes observaciones:

| Horas de estudio | Horas de sueño | Aprobado (1) / No aprobado (0) |
|------------------|----------------|--------------------------------|
| 5                | 7              | 1                              |
| 3                | 6              | 0                              |
| 8                | 5              | 1                              |
| 2                | 8              | 0                              |

El modelo de regresión logística utilizará estos datos para ajustar los coeficientes \( b_0 \), \( b_1 \) y \( b_2 \) de manera que las predicciones sean lo más precisas posible.

## Resumen

- Los coeficientes \( b_0 \), \( b_1 \) y \( b_2 \) no son aleatorios; se obtienen a través del proceso de entrenamiento del modelo.
- Este proceso implica ajustar los coeficientes para minimizar la diferencia entre las predicciones del modelo y las etiquetas reales en los datos de entrenamiento.

# Ejemplo Práctico de Regresión Logística

## Conjunto de Datos

Imagina que tienes el siguiente conjunto de datos:

| Horas de estudio | Horas de sueño | Aprobado (1) / No aprobado (0) |
|------------------|----------------|--------------------------------|
| 5                | 7              | 1                              |
| 3                | 6              | 0                              |
| 8                | 5              | 1                              |
| 2                | 8              | 0                              |

## Paso 1: Importar las librerías necesarias

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Crear un DataFrame con los datos
data = {
    'Horas de estudio': [5, 3, 8, 2],
    'Horas de sueño': [7, 6, 5, 8],
    'Aprobado': [1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Separar las características (X) y la etiqueta (y)
X = df[['Horas de estudio', 'Horas de sueño']]
y = df['Aprobado']

# Crear y entrenar el modelo
model = LogisticRegression()
model.fit(X, y)
# Obtener los coeficientes
b0 = model.intercept_[0]
b1, b2 = model.coef_[0]

print(f"b0 (intersección): {b0}")
print(f"b1 (coeficiente para Horas de estudio): {b1}")
print(f"b2 (coeficiente para Horas de sueño): {b2}")

```

##Resultados
Después de ejecutar el código, obtendrás los siguientes valores para los coeficientes:

b0 (intersección): Este es el término de intersección del modelo.

b1 (coeficiente para Horas de estudio): Este es el coeficiente que multiplica las horas de estudio.

b2 (coeficiente para Horas de sueño): Este es el coeficiente que multiplica las horas de sueño.

Los valores específicos de 𝑏0, 𝑏1 y 𝑏2 dependerán de los datos de entrenamiento y del ajuste del modelo. Aquí tienes un ejemplo de los posibles resultados:

b0 (intersección): -1.5
b1 (coeficiente para Horas de estudio): 0.8
b2 (coeficiente para Horas de sueño): 0.3

Estos valores indican cómo cada característica (horas de estudio y horas de sueño) afecta la probabilidad de que un estudiante apruebe el examen. El término de intersección 
𝑏
0
 ajusta la línea de decisión del modelo.

## Entropía Cruzada

La entropía cruzada es una medida utilizada en aprendizaje automático y teoría de la información para cuantificar la diferencia entre dos distribuciones de probabilidad. En el contexto de los modelos de clasificación, se utiliza para evaluar qué tan bien las predicciones del modelo se alinean con las etiquetas reales.

### Concepto Básico

Imagina que tienes un modelo que predice la probabilidad de que una observación pertenezca a una clase particular. La entropía cruzada mide la "diferencia" entre las probabilidades predichas por el modelo y las probabilidades reales (que son 1 para la clase correcta y 0 para las demás).

### Fórmula

La fórmula de la entropía cruzada para un conjunto de datos con \( n \) observaciones y \( k \) clases es:



\[ H(p, q) = - \sum_{i=1}^{n} \sum_{j=1}^{k} p_{ij} \log(q_{ij}) \]



Donde:
- \( p_{ij} \) es la probabilidad real de que la observación \( i \) pertenezca a la clase \( j \) (que es 1 si la observación pertenece a la clase \( j \) y 0 en caso contrario).
- \( q_{ij} \) es la probabilidad predicha por el modelo de que la observación \( i \) pertenezca a la clase \( j \).

### Ejemplo Práctico

Supongamos que tienes un modelo que predice si un correo electrónico es spam (1) o no spam (0). Para un conjunto de correos electrónicos, el modelo predice las siguientes probabilidades:

| Correo | Probabilidad de ser spam (predicha) | Etiqueta real |
|--------|-------------------------------------|---------------|
| 1      | 0.9                                 | 1             |
| 2      | 0.4                                 | 0             |
| 3      | 0.7                                 | 1             |
| 4      | 0.2                                 | 0             |

La entropía cruzada se calcularía como:



\[ H(p, q) = - [1 \cdot \log(0.9) + 0 \cdot \log(0.1) + 0 \cdot \log(0.4) + 1 \cdot \log(0.6) + 1 \cdot \log(0.7) + 0 \cdot \log(0.3) + 0 \cdot \log(0.2) + 1 \cdot \log(0.8)] \]



### Simplificación

Al simplificar, los términos con \( 0 \cdot \log(\text{probabilidad}) \) se eliminan porque cualquier número multiplicado por 0 es 0. Así que solo quedan los términos relevantes:



\[ H(p, q) = - [\log(0.9) + \log(0.6) + \log(0.7) + \log(0.8)] \]



### Interpretación

- **Baja entropía cruzada**: Indica que las predicciones del modelo están muy cerca de las etiquetas reales.
- **Alta entropía cruzada**: Indica que hay una gran diferencia entre las predicciones del modelo y las etiquetas reales.

## Resumen

La entropía cruzada es una métrica crucial para entrenar y evaluar modelos de clasificación como la regresión logística. Ayuda a asegurarse de que el modelo esté aprendiendo correctamente y haciendo buenas predicciones.

# Interpretación de la Entropía Cruzada

## ¿Qué es la Entropía Cruzada?

La entropía cruzada es una medida utilizada en aprendizaje automático y teoría de la información para cuantificar la diferencia entre dos distribuciones de probabilidad. En el contexto de los modelos de clasificación, se utiliza para evaluar qué tan bien las predicciones del modelo se alinean con las etiquetas reales.

## Interpretación de la Entropía Cruzada

### Valor Absoluto

La entropía cruzada es una medida de error, por lo que un valor más bajo indica un mejor rendimiento del modelo. No hay un valor "universal" que defina baja o alta entropía cruzada, ya que depende del contexto y del problema específico.

### Comparación Relativa

Compara la entropía cruzada de tu modelo con la de otros modelos o con la entropía cruzada de un modelo base (por ejemplo, un modelo que siempre predice la clase más frecuente). Si tu modelo tiene una entropía cruzada significativamente menor, entonces está funcionando bien.

### Escala de Valores

En general, para problemas de clasificación binaria, una entropía cruzada cercana a 0 indica un modelo muy preciso. Valores más altos indican mayor error. Por ejemplo:

- **Muy baja**: < 0.1 (excelente rendimiento)
- **Baja**: 0.1 - 0.5 (buen rendimiento)
- **Moderada**: 0.5 - 1.0 (rendimiento aceptable)
- **Alta**: > 1.0 (rendimiento pobre)

## Ejemplo Práctico

En tu ejemplo, calculamos la entropía cruzada como:



\[ H(p, q) = - [\log(0.9) + \log(0.6) + \log(0.7) + \log(0.8)] \]



### Calculando los valores:

- \(\log(0.9) \approx -0.105\)
- \(\log(0.6) \approx -0.511\)
- \(\log(0.7) \approx -0.357\)
- \(\log(0.8) \approx -0.223\)

### Sumando estos valores:



\[ H(p, q) = - [-0.105 + -0.511 + -0.357 + -0.223] = 1.196 \]



## Interpretación del Resultado

En este caso, una entropía cruzada de 1.196 sugiere que el modelo tiene un rendimiento moderado a pobre. Esto indica que hay espacio para mejorar el modelo, ya sea ajustando los hiperparámetros, utilizando más datos de entrenamiento, o probando diferentes algoritmos de clasificación.

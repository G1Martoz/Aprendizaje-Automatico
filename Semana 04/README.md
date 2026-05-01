# � Semana 04: Regresión Lineal y Logística

Este directorio contiene las actividades correspondientes a la cuarta semana del curso, enfocadas en la implementación de modelos de aprendizaje supervisado.

## 🗺️ Guía de Navegación

A continuación se detallan los archivos principales y su propósito dentro de la carpeta `Semana 04`:

### 1. Actividad de Regresión Lineal Simple
*   **Notebook:** [regresion_lineal.ipynb](regresion_lineal.ipynb)
*   **Dataset:** [Salary_Data.csv](Salary_Data.csv)
*   **Descripción:** En este ejercicio se predice el salario en función de los años de experiencia.
*   **Gráfico Correspondiente:** Al final del notebook se encuentra el gráfico de dispersión con la **Recta de Regresión** que visualiza el ajuste del modelo.

### 2. Actividad de Regresión Logística (Clasificación)
*   **Notebook:** [regresion_logistica.ipynb](regresion_logistica.ipynb)
*   **Dataset:** [usuarios_win_mac_lin.csv](usuarios_win_mac_lin.csv)
*   **Descripción:** Modelo de clasificación multiclase (Windows, Mac, Linux) basado en el comportamiento web de los usuarios.
*   **Gráfico Correspondiente:** Incluye una **Matriz de Confusión de 3x3** para analizar detalladamente los falsos positivos y la precisión del modelo en cada clase.

---

## ⚠️ Casos de Prueba (Ignorables)
Los siguientes archivos fueron utilizados únicamente como **pruebas piloto** o análisis preliminares y **no forman parte de la entrega final** de la tarea:
*   [PPiloto.ipynb](PPiloto.ipynb)
*   [EDA.ipynb](EDA.ipynb)

---

## 🔬 Interpretación de Resultados

*   **Regresión Lineal:** El modelo muestra una correlación muy fuerte entre la experiencia y el salario, con un coeficiente $R^2$ alto que confirma su robustez.
*   **Regresión Logística:** La matriz de confusión permite identificar visualmente las fronteras de decisión y cómo el modelo separa a los usuarios según su sistema operativo.

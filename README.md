# Tarea 3: Polars
Ana María Ramírez

## Descripción del problema

Este proyecto tiene como objetivo analizar y predecir la duración de viajes de taxi en Nueva York, utilizando técnicas de procesamiento de datos y aprendizaje automático. Se trabajó con un problema de regresión supervisada donde la variable objetivo corresponde a la duración total del viaje (trip_duration) medida en segundos. El proyecto fue desarrollado utilizando Polars como herramienta principal para procesamiento de datos, y se realizó una comparación experimental contra Pandas para evaluar rendimiento, escalabilidad y tiempos de ejecución.

El flujo del proyecto incluye:

- Análisis Exploratorio de Datos (EDA)
- Ingeniería de Características
- Entrenamiento de modelos de Machine Learning
- Benchmark Polars vs Pandas
- Experimentos de escalabilidad
- Evaluación de Lazy Execution

## Fuente del dataset

- Dataset utilizado: NYC Taxi Trip Duration (Kaggle)

Características del dataset:
- Problema de regresión
- Aproximadamente 1.46 millones de registros
-Variables numéricas, temporales y categóricas

Debido a las restricciones de tamaño de GitHub, los archivos de datos utilizados en este proyecto no se incluyen dentro del repositorio. En particular, los datasets originales y los archivos procesados fueron excluidos. Para ejecutar el proyecto correctamente, se debe descargar el conjunto de datos correspondiente y colocarlo en la carpeta indicada dentro de la estructura del proyecto antes de correr el código. Esto permite mantener un repositorio más liviano, facilitar la clonación y cumplir con las limitaciones de almacenamiento de GitHub.

Enlace de Kaggle: https://www.kaggle.com/datasets/yasserh/nyc-taxi-trip-duration

## Requisitos de Software

Entorno recomendado:
- Google Colab o Jupyter Notebook
- Git

Librerías principales:
- polars
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- xgboost
- pyarrow
- psutil

## Instrucciones de Instalación

1. Clonar el repositorio:
git clone URL_DEL_REPOSITORIO

2. Entrar al proyecto:
cd project

3. Instalar dependencias.

4. Descargar el dataset
Descargar el archivo NYC.csv desde Kaggle y colocarlo en:
data/raw/

## Instrucciones de Ejecución
### Ejecutar análisis completo

1. Abrir:
notebooks/analysis.ipynb

2. Ejecutar todas las celdas en orden.

El notebook realiza automáticamente:
- Carga del dataset
- EDA utilizando Polars
- Ingeniería de características
- Entrenamiento de modelos
- Benchmark Polars vs Pandas
- Experimentos de escalabilidad
- Generación de resultados y gráficas

### Ejecutar módulos individualmente

3. Preprocesamiento:

python src/preprocessing.py

4. Feature Engineering:

python src/feature_engineering.py

5. Entrenamiento:

python src/train_models.py

6. Benchmark Polars:

python src/polars_pipeline.py

7. Benchmark Pandas:

python src/pandas_pipeline.py

## Resumen de Resultados Obtenidos

### Resultados de Machine Learning

| Modelo            | RMSE   | MAE    |
| ----------------- | ------ | ------ |
| Regresión Lineal  | 432.37 | 287.96 |
| Random Forest     | 258.49 | 175.57 |
| Gradient Boosting | 299.19 | 209.04 |


El modelo con mejor desempeño fue Random Forest.

### Benchmark Polars vs Pandas

| Operación      | Speedup |
| -------------- | ------- |
| Lectura        | 3.64×   |
| Filtrado       | 2.55×   |
| Agregación     | 2.34×   |
| Join           | 5.85×   |
| Pipeline Total | 2.92×   |


Polars redujo aproximadamente un 66 % del tiempo total respecto a Pandas.

### Escalabilidad

| Dataset | Speedup |
| ------- | ------- |
| 25 %    | 1.25×   |
| 50 %    | 3.07×   |
| 75 %    | 2.85×   |
| 100 %   | 2.82×   |


Los resultados mostraron que el beneficio de Polars aumenta conforme incrementa el tamaño del conjunto de datos.

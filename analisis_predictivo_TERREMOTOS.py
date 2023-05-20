import numpy as np
import matplotlib.pyplot as plt

# Datos históricos
magnitudes = np.array([5.6, 6.1, 4.9, 5.2, 6.5, 7.8, 5.7, 6.3, 4.9, 8.1, 6.5])  # Magnitudes de los terremotos
ubicaciones = np.array(['A', 'B', 'C', 'A', 'B', 'C', 'C', 'A', 'A', 'B', 'C'])  # Ubicaciones geográficas

# Función para muestrear de la distribución posterior
def muestra_posterior(magnitudes, ubicaciones, nueva_ubicacion, num_muestras=1000):
    ubicaciones_unicas = np.unique(ubicaciones)
    num_ubicaciones = len(ubicaciones_unicas)
    
    # Filtrar las magnitudes por la ubicación
    magnitudes_filtradas = magnitudes[ubicaciones == nueva_ubicacion]
    
    if len(magnitudes_filtradas) == 0:
        print(f"No hay datos disponibles para la ubicación {nueva_ubicacion}.")
        return None
    
    # Estimación de los parámetros
    media_post = np.mean(magnitudes_filtradas)
    desviacion_post = np.std(magnitudes_filtradas)
    
    # Muestreo de la distribución posterior predictiva
    nuevas_muestras_magnitud = np.random.normal(loc=media_post, scale=desviacion_post, size=num_muestras)
    
    return nuevas_muestras_magnitud
# Predicción para una nueva ubicación
nueva_ubicacion = 'B'
nuevas_muestras_magnitud = muestra_posterior(magnitudes, ubicaciones, nueva_ubicacion)
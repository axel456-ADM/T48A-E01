import numpy as np
import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "Axel De Avila Martinez"
numero_de_matricula = 177499
fecha = '2025-11-09'

def capitalizacion():
    # inserta tu código aquí
    datos = [17, 21, 44, 50, 79, 86, 140, 178, 203]
    media = np.mean(datos)
    mediana = np.median(datos)
    moda = pd.Series(datos).mode()[0]
    desv_est = np.std(datos)
    return (media, mediana, moda, desv_est)

def asistencia_dispersion():
    # inserta tu código aquí:
    asistencias = [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]
    rango = np.max(asistencias) - np.min(asistencias)
    varianza = np.var(asistencias)
    desv_est = np.std(asistencias)

    return (rango, varianza, desv_est)

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]

    hist, bordes = np.histogram(calificaciones, bordes='auto')  
    
    return (hist, bordes)

from scipy.stats import pearsonr

def correlacion():
    tamano = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
    precio = [1385710, 1658277, 1894167, 2136552, 2298267, 2553624, 2788053, 3289726, 3472743, 3779477]

    coeficiente, _ = pearsonr(tamano, precio)
    
    return coeficiente



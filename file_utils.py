import os
import scipy.io as sio

def buscar_archivo(archivo_nombre, carpeta_inicio="."):
    """
    Busca un archivo específico dentro de una carpeta o subcarpetas.
    
    Parámetros:
    -----------
    archivo_nombre : str
        El nombre del archivo que se busca (ej: 'S1.mat').
    carpeta_inicio : str, opcional
        La carpeta desde la que comienza la búsqueda (por defecto es la carpeta actual).
    
    Retorna:
    --------
    str o None
        Retorna la ruta completa del archivo si se encuentra, de lo contrario, retorna None.
    """
    for root, dirs, files in os.walk(carpeta_inicio):  # Busca en todas las subcarpetas
        if archivo_nombre in files:
            return os.path.join(root, archivo_nombre)  # Retorna la ruta completa
    return None  # Si no se encuentra el archivo


def cargar_archivo_mat(archivo_nombre):
    """
    Busca y carga un archivo .mat automáticamente.
    
    Parámetros:
    -----------
    archivo_nombre : str
        El nombre del archivo .mat (ej: 'S1.mat').
    
    Retorna:
    --------
    numpy.ndarray
        Señal de EEG cargada desde el archivo .mat.
    """
    print(f"Buscando {archivo_nombre}...")
    ruta_archivo = buscar_archivo(archivo_nombre, os.path.expanduser("~"))  # Buscar en la carpeta de usuario

    if ruta_archivo:
        print(f"Archivo encontrado: {ruta_archivo}")
        mat_data = sio.loadmat(ruta_archivo)
        signal_data = mat_data['data']
        return signal_data
    else:
        raise FileNotFoundError(f"No se encontró el archivo {archivo_nombre}")

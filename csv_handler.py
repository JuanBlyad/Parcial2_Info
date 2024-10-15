import pandas as pd
import matplotlib.pyplot as plt
import os

def buscar_archivo(archivo_nombre, carpeta_inicio="."):
    """
    Busca un archivo específico dentro de una carpeta o subcarpetas.
    
    Parámetros:
    -----------
    archivo_nombre : str
        El nombre del archivo que se busca (ej: 'archivo.csv').
    carpeta_inicio : str, opcional
        La carpeta desde la que comienza la búsqueda (por defecto es la carpeta actual).
    
    Retorna:
    --------
    str o None
        Retorna la ruta completa del archivo si se encuentra, de lo contrario, retorna None.
    """
    for root, dirs, files in os.walk(carpeta_inicio):
        if archivo_nombre in files:
            return os.path.join(root, archivo_nombre)
    return None

class CSVFileHandler:
    """
    Clase encargada de manejar archivos CSV.
    Permite cargar el archivo, manejar NaN, realizar operaciones entre columnas y graficar.
    """

    def __init__(self, file_path):
        """
        Inicializa la clase buscando y cargando el archivo CSV.
        """
        # Buscar el archivo CSV en las carpetas del sistema
        ruta_archivo = buscar_archivo(file_path, ".")  # Busca en el directorio actual
        if ruta_archivo:
            try:
                self.data = pd.read_csv(ruta_archivo)
                print(f"Archivo {ruta_archivo} cargado correctamente con dimensiones: {self.data.shape}")
            except pd.errors.EmptyDataError:
                print(f"Error: El archivo {file_path} está vacío o no es un CSV válido.")
        else:
            raise FileNotFoundError(f"No se encontró el archivo {file_path}")

    def contar_nan(self):
        """Cuenta cuántos valores NaN hay por columna."""
        nan_counts = self.data.isna().sum()
        print(f"Valores NaN por columna:\n{nan_counts}")
        return nan_counts

    def limpiar_datos(self):
        """Limpia los registros con valores NaN y retorna el DataFrame limpio."""
        self.data = self.data.dropna()
        print(f"Datos después de la limpieza: {self.data.shape}")

    def agregar_columna(self, col1, col2, nueva_col):
        """Crea una nueva columna como multiplicación de dos columnas numéricas."""
        # Verificar si las columnas existen en el DataFrame
        if col1 not in self.data.columns:
            print(f"Error: La columna '{col1}' no existe en el archivo.")
            return
        if col2 not in self.data.columns:
            print(f"Error: La columna '{col2}' no existe en el archivo.")
            return
        # Si las columnas existen, proceder con la multiplicación
        self.data[nueva_col] = self.data[col1] * self.data[col2]
        print(f"Nueva columna '{nueva_col}' creada como multiplicación de {col1} y {col2}.")

    def guardar_csv(self, output_path):
        """Guarda el DataFrame en un archivo CSV."""
        self.data.to_csv(output_path, index=False)
        print(f"Datos guardados en el archivo: {output_path}")

    def graficar_datos(self, col1, col2):
        """Genera dos tipos de gráficos para las columnas especificadas."""
        if col1 not in self.data.columns or col2 not in self.data.columns:
            print(f"Error: Las columnas '{col1}' o '{col2}' no existen en el archivo.")
            return
        
        plt.figure(figsize=(12, 5))

        # Gráfico 1: Línea
        plt.subplot(1, 2, 1)
        plt.plot(self.data[col1], label=col1)
        plt.plot(self.data[col2], label=col2)
        plt.title('Gráfico de líneas')
        plt.xlabel('Índice')
        plt.ylabel('Valores')
        plt.legend()

        # Gráfico 2: Barras
        plt.subplot(1, 2, 2)
        plt.bar(self.data.index, self.data[col1], label=col1)
        plt.bar(self.data.index, self.data[col2], label=col2)
        plt.title('Gráfico de barras')
        plt.xlabel('Índice')
        plt.ylabel('Valores')
        plt.legend()

        plt.tight_layout()
        plt.show()

    


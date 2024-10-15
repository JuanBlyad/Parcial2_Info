import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from file_utils import cargar_archivo_mat  # Importar la función para cargar el archivo mat

class MatFileHandler:
    """
    Clase encargada de manejar archivos .mat.
    Permite cargar el archivo, transformar la matriz a 2D, realizar operaciones entre canales, y graficar.
    """

    def __init__(self, file_path):
        # Cargar archivo usando la función de búsqueda
        self.data = cargar_archivo_mat(file_path)
        self.time = np.linspace(0, 1, self.data.shape[1])  # Tiempo ajustado al número de muestras reales

    def transformar_2D(self):
        """Convierte la matriz original a 2D unificando las épocas."""
        self.data = self.data.reshape(self.data.shape[0], -1)  # Transformar a 2D
        self.time = np.linspace(0, 1, self.data.shape[1])  # Ajustar el tiempo al nuevo tamaño
        print(f"Datos transformados a 2D con nueva forma: {self.data.shape}")

    def operaciones_canales(self, canal_1, canal_2, canal_3):
        """
        Realiza operaciones entre tres canales: resta, multiplicación, y agrega ruido.
        """
        resta = self.data[canal_1] - self.data[canal_2]
        multiplicacion = self.data[canal_1] * self.data[canal_3]
        ruido = multiplicacion + np.random.normal(0, 0.1, size=multiplicacion.shape)

        return resta, multiplicacion, ruido

    def graficar_operaciones(self, canal_1, canal_2, canal_3):
        """Genera tres gráficos mostrando las operaciones entre los canales en un layout específico."""
        resta, multiplicacion, ruido = self.operaciones_canales(canal_1, canal_2, canal_3)

        fig = plt.figure(figsize=(12, 8))

        # Estructura de gráficos: uno grande a la izquierda, dos pequeños a la derecha
        ax1 = plt.subplot2grid((2, 3), (0, 0), rowspan=2, colspan=2)  # Gráfico grande
        ax2 = plt.subplot2grid((2, 3), (0, 2))  # Primer gráfico pequeño
        ax3 = plt.subplot2grid((2, 3), (1, 2))  # Segundo gráfico pequeño

        # Gráfico 1: Resta
        ax1.plot(self.time, resta, label=f'Resta: Canal {canal_1+1} - Canal {canal_2+1}')
        ax1.set_title('Resta entre canales')
        ax1.set_xlabel('Tiempo (s)')
        ax1.set_ylabel('Amplitud')
        ax1.legend()
        ax1.grid(True)

        # Gráfico 2: Multiplicación
        ax2.plot(self.time, multiplicacion, label=f'Multiplicación: Canal {canal_1+1} * Canal {canal_3+1}')
        ax2.set_title('Multiplicación entre canales')
        ax2.set_xlabel('Tiempo (s)')
        ax2.set_ylabel('Amplitud')
        ax2.legend()
        ax2.grid(True)

        # Gráfico 3: Ruido
        ax3.plot(self.time, ruido, label='Resultado con ruido añadido')
        ax3.set_title('Multiplicación con ruido')
        ax3.set_xlabel('Tiempo (s)')
        ax3.set_ylabel('Amplitud')
        ax3.legend()
        ax3.grid(True)

        plt.tight_layout()
        plt.show()

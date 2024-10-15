from mat_handler import MatFileHandler
from csv_handler import CSVFileHandler

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Cargar y analizar archivo .mat")
        print("2. Cargar y analizar archivo .csv")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == '1':
            file_path = input("Ingrese el nombre del archivo .mat: ")
            try:
                mat_handler = MatFileHandler(file_path)
                mat_handler.transformar_2D()

                # Solicitar los canales al usuario
                canal_1 = int(input("Ingrese el canal 1: ")) - 1
                canal_2 = int(input("Ingrese el canal 2: ")) - 1
                canal_3 = int(input("Ingrese el canal 3: ")) - 1

                # Graficar las operaciones entre los canales
                mat_handler.graficar_operaciones(canal_1, canal_2, canal_3)

            except FileNotFoundError as e:
                print(e)

        elif opcion == '2':
            file_path = input("Ingrese el nombre del archivo .csv: ")
            try:
                csv_handler = CSVFileHandler(file_path)

                # Contar y limpiar NaN
                csv_handler.contar_nan()
                csv_handler.limpiar_datos()

                # Solicitar columnas para crear nueva columna y graficar
                col1 = input("Ingrese la primera columna numérica: ")
                col2 = input("Ingrese la segunda columna numérica: ")
                nueva_col = input("Ingrese el nombre para la nueva columna: ")
                csv_handler.agregar_columna(col1, col2, nueva_col)

                # Guardar archivo CSV modificado
                output_path = input("Ingrese la ruta para guardar el archivo CSV modificado: ")
                csv_handler.guardar_csv(output_path)

                # Graficar los datos
                csv_handler.graficar_datos(col1, col2)

            except FileNotFoundError as e:
                print(e)

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()

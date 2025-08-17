from arbol_b import ArbolB
from clase_tipo_dato import Trabajador


def menu():
    print("\n--- Menú de Gestión de Proveedores ---")
    print("1. Insertar nuevo proveedor")
    print("2. Buscar proveedores por tipo de servicio")
    print("3. Listar todos los proveedores ordenados por ID")
    print("4. Listar proveedores ordenados por Nombre")
    print("5. Listar proveedores ordenados por Calificación")
    print("0. Salir")
    return input("Seleccione una opción: ")


def leer_entero(mensaje):
    """Lee un entero con validación."""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("⚠️ Error: debe ingresar un número entero.")


def leer_flotante(mensaje):
    """Lee un número decimal con validación."""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("⚠️ Error: debe ingresar un número decimal (ej: 4.5).")


def main():
    orden = 4  # puedes ajustar el orden del árbol B
    arbol = ArbolB(orden)

    # 🔹 Proveedores precargados
    precargados = [
        Trabajador(10, "Carlos Fuentes", "Electricista", 4.5),
        Trabajador(5, "Ana Orozco", "Contadora", 4.8),
        Trabajador(20, "Luis Sac", "Carpintero", 4.2),
        Trabajador(15, "María Salic", "Plomero", 4.9),
        Trabajador(8, "Josue Ixquiac", "Albañil", 4.0),
        Trabajador(25, "José Interiano", "Electricista", 3.9),
        Trabajador(18, "Victoria de León", "Contadora", 4.7),
    ]

    for p in precargados:
        arbol.insertar(p)

    print("✅ Proveedores precargados en el sistema.")

    while True:
        opcion = menu()

        if opcion == "1":
            id = leer_entero("Ingrese ID del proveedor: ")
            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo de servicio (ej: plomero, electricista): ")
            calificacion = leer_flotante("Ingrese calificación (0-5): ")

            trabajador = Trabajador(id, nombre, tipo, calificacion)
            arbol.insertar(trabajador)
            print("Proveedor registrado exitosamente ✅")

        elif opcion == "2":
            tipo = input("Ingrese el tipo de servicio a buscar: ")
            resultados = arbol.buscar(arbol.raiz, tipo)

            if resultados:
                print(f"\nProveedores que ofrecen '{tipo}':")
                for r in resultados:
                    print(r)
            else:
                print("No se encontraron proveedores con ese servicio.")

        elif opcion == "3":
            lista = arbol.recorrido_inorden(arbol.raiz)
            print("\n--- Proveedores ordenados por ID ---")
            for r in lista:
                print(r)

        elif opcion == "4":
            lista = arbol.recorrido_inorden(arbol.raiz)
            lista.sort(key=lambda x: x.nombre.lower())
            print("\n--- Proveedores ordenados por Nombre ---")
            for r in lista:
                print(r)

        elif opcion == "5":
            lista = arbol.recorrido_inorden(arbol.raiz)
            lista.sort(key=lambda x: x.calificacion, reverse=True)
            print("\n--- Proveedores ordenados por Calificación ---")
            for r in lista:
                print(r)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()

from arbol_b import ArbolB
from clase_tipo_dato import Trabajador


def main():
    # Crear árbol B de orden 3
    arbol = ArbolB(3)

    # Insertar trabajadores en el árbol
    arbol.insertar(Trabajador(10, "Luis", "Electricista", 5))
    arbol.insertar(Trabajador(5, "Ana", "Plomero", 4))
    arbol.insertar(Trabajador(20, "Carlos", "Electricista", 3))
    arbol.insertar(Trabajador(15, "Maria", "Carpintero", 5))
    arbol.insertar(Trabajador(25, "Jose", "Plomero", 2))
    arbol.insertar(Trabajador(30, "Pedro", "Carpintero", 4))
    arbol.insertar(Trabajador(2, "Elena", "Electricista", 5))

    # Mostrar recorrido en orden
    print("🔹 Trabajadores ordenados por ID (recorrido inorden):")
    for trabajador in arbol.recorrido_inorden(arbol.raiz):
        print(trabajador)

    # Buscar todos los plomeros
    print("\n🔹 Buscando Plomeros en el árbol:")
    plomeros = arbol.buscar(arbol.raiz, "Plomero")
    if plomeros:
        for p in plomeros:
            print(p)
    else:
        print("No se encontraron plomeros.")

    # Buscar electricistas
    print("\n🔹 Buscando Electricistas en el árbol:")
    electricistas = arbol.buscar(arbol.raiz, "Electricista")
    if electricistas:
        for e in electricistas:
            print(e)
    else:
        print("No se encontraron electricistas.")


if __name__ == "__main__":
    main()

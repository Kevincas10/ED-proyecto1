from nodo_b import NodoB


class ArbolB:
    def __init__(self, orden):
        self.orden = orden
        self.raiz = NodoB(orden)

    def buscar(self, nodo, servicio):
        # Busca recursivamente todos los trabajadores con el tipo de servicio especificado
        resultados = []
        i = 0
        while i < len(nodo.claves):
            if not nodo.hoja:
                # Buscar primero en el hijo izquierdo antes de la clave actual
                resultados.extend(self.buscar(nodo.hijos[i], servicio))

            # Verificar si el proveedor en la clave actual tiene el servicio buscado
            if nodo.proveedores[i].tipo_servicio == servicio:
                resultados.append(nodo.proveedores[i])

            i += 1

        # Finalmente, buscar en el último hijo (derecho)
        if not nodo.hoja:
            resultados.extend(self.buscar(nodo.hijos[i], servicio))

        return resultados

    def recorrido_inorden(self, nodo, lista=None):
        # Recorre el árbol en inorden para devolver trabajadores ordenados por ID
        if lista is None:
            lista = []

        for i in range(len(nodo.claves)):
            if not nodo.hoja:
                # Recorrer el hijo izquierdo antes de la clave
                self.recorrido_inorden(nodo.hijos[i], lista)

            # Agregar el proveedor correspondiente a la clave actual
            lista.append(nodo.proveedores[i])

        # Recorrer el último hijo después de la última clave
        if not nodo.hoja:
            self.recorrido_inorden(nodo.hijos[len(nodo.claves)], lista)

        return lista

    def dividir_nodo(self, padre, indice, nodo):
        # Divide un nodo lleno en dos nodos y sube la clave del medio al padre

        # Calcular índice de la clave media
        t = self.orden // 2

        # Crear un nuevo nodo que almacenará la mitad derecha
        nuevo = NodoB(self.orden, nodo.hoja)

        # Copiar claves y proveedores de la mitad derecha al nuevo nodo
        nuevo.claves = nodo.claves[t + 1:]
        nuevo.proveedores = nodo.proveedores[t + 1:]

        # Si no es hoja, también mover los hijos derechos
        if not nodo.hoja:
            nuevo.hijos = nodo.hijos[t + 1:]

        # Guardar la clave y proveedor que van a subir al padre
        clave_media = nodo.claves[t]
        proveedor_medio = nodo.proveedores[t]

        # Reducir el nodo original a la mitad izquierda
        nodo.claves = nodo.claves[:t]
        nodo.proveedores = nodo.proveedores[:t]
        if not nodo.hoja:
            nodo.hijos = nodo.hijos[:t + 1]

        # Insertar en el padre la clave media y el nuevo nodo como hijo derecho
        padre.claves.insert(indice, clave_media)
        padre.proveedores.insert(indice, proveedor_medio)
        padre.hijos.insert(indice + 1, nuevo)

    def insertar_no_lleno(self, nodo, proveedor):
        # Inserta un trabajador en un nodo que no está lleno
        i = len(nodo.claves) - 1

        if nodo.hoja:
            # Si es hoja, se inserta en la posición correcta manteniendo orden
            nodo.claves.append(None)
            nodo.proveedores.append(None)

            # Desplazar claves/proveedores mayores hacia la derecha
            while i >= 0 and proveedor.id < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                nodo.proveedores[i + 1] = nodo.proveedores[i]
                i -= 1

            # Insertar en la posición encontrada
            nodo.claves[i + 1] = proveedor.id
            nodo.proveedores[i + 1] = proveedor

        else:
            # Si no es hoja, buscar el hijo correcto para insertar
            while i >= 0 and proveedor.id < nodo.claves[i]:
                i -= 1
            i += 1

            # Si el hijo está lleno, dividirlo primero
            if len(nodo.hijos[i].claves) == self.orden - 1:
                self.dividir_nodo(nodo, i, nodo.hijos[i])
                # Decidir en qué hijo continuar después de la división
                if proveedor.id > nodo.claves[i]:
                    i += 1

            # Llamada recursiva para insertar en el hijo correcto
            self.insertar_no_lleno(nodo.hijos[i], proveedor)

    def insertar(self, proveedor):
        # Inserta un nuevo trabajador en el árbol
        # Si la raíz está llena, se divide y se crea una nueva raíz
        raiz = self.raiz
        if len(raiz.claves) == self.orden - 1:
            nuevo_nodo = NodoB(self.orden, hoja=False)
            nuevo_nodo.hijos.append(raiz)
            self.raiz = nuevo_nodo
            self.dividir_nodo(nuevo_nodo, 0, raiz)
            self.insertar_no_lleno(nuevo_nodo, proveedor)
        else:
            # Si no está llena, se inserta directamente
            self.insertar_no_lleno(raiz, proveedor)

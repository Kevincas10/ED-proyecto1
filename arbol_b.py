from nodo_b import NodoB


class ArbolB:
    def __init__(self, orden):
        self.orden = orden  # Orden del árbol B
        self.raiz = NodoB(orden)  # Nodo raíz, inicialmente hoja vacío

    def buscar(self, nodo, servicio):
        # busca recursivmente a todos los proveedores con el tipo de servicio
        # lo recorre visitando hijos y claves
        resultados = []
        i = 0
        while i < len(nodo.claves):
            if not nodo.hoja:
                # Buscar en el hijo izquierdo antes de la clave
                resultados.extend(self.buscar(nodo.hijos[i], servicio))
            # Verificar si el proveedor en la clave actual tiene el servicio buscado
            if hasattr(nodo.proveedores[i], 'servicio') and nodo.proveedores[i].servicio == servicio:
                resultados.append(nodo.proveedores[i])
            i += 1
        # Buscar también en el último hijo -> derecho
        if not nodo.hoja:
            resultados.extend(self.buscar(nodo.hijos[i], servicio))
        return resultados

    def recorrido_inorden(self, nodo, lista=None):
        # Recorre el arbol in-order para obtener un lista ordenada por ID
        if lista is None:
            lista = []
        for i in range(len(nodo.claves)):
            if not nodo.hoja:
                # Recorrer el hijo izquierdo antes de la clave
                self.recorrido_inorden(nodo.hijos[i], lista)
            # Agregar el proveedor asociado a la clave
            lista.append(nodo.proveedores[i])
        # Recorrer el último hijo después de la última clave
        if not nodo.hoja:
            self.recorrido_inorden(nodo.hijos[len(nodo.claves)], lista)
        return lista

    def dividir_nodo(self, padre, indice, nodo):
        # Divide el nodo lleno en dos y mueve la clase del medio al nodo padre
        # Índice de la clave media
        t = self.orden // 2
        # Nuevo nodo que contendrá la mitad derecha
        nuevo = NodoB(self.orden, nodo.hoja)  # Nuevo nodo que contendrá la mitad derecha

        # Copiar las claves y proveedores derechos al nuevo nodo
        nuevo.claves = nodo.claves[t + 1:]
        nuevo.proveedores = nodo.proveedores[t + 1:]

        # Si no es hoja, también mover los hijos derechos al nuevo nodo
        if not nodo.hoja:
            nuevo.hijos = nodo.hijos[t + 1:]

        # Reducir el nodo original a la mitad izquierda
        nodo.claves = nodo.claves[:t]
        nodo.proveedores = nodo.proveedores[:t]
        if not nodo.hoja:
            nodo.hijos = nodo.hijos[:t + 1]

        # Insertar la clave media y su proveedor en el padre
        padre.claves.insert(indice, nodo.claves[t])
        padre.proveedores.insert(indice, nodo.proveedores[t])
        # Insertar el nuevo nodo como hijo derecho en la posición correcta
        padre.hijos.insert(indice + 1, nuevo)

        # Remover la clave y proveedor media del nodo original (porque subió al padre)
        nodo.claves.pop(t)
        nodo.proveedores.pop(t)

    def insertar_no_lleno(self, nodo, proveedor):
        # Inserta un proveedor en un nodo que no esta lleno
        i = len(nodo.claves) - 1
        if nodo.hoja:
            # Insertar en la posición correcta para mantener orden
            nodo.claves.append(None)
            nodo.proveedores.append(None)
            while i >= 0 and proveedor.id < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                nodo.proveedores[i + 1] = nodo.proveedores[i]
                i -= 1
            nodo.claves[i + 1] = proveedor.id
            nodo.proveedores[i + 1] = proveedor
        else:
            # Encontrar el hijo correcto para insertar
            while i >= 0 and proveedor.id < nodo.claves[i]:
                i -= 1
            i += 1
            # Si el hijo está lleno, dividirlo primero
            if len(nodo.hijos[i].claves) == self.orden - 1:
                self.dividir_nodo(nodo, i, nodo.hijos[i])
                if proveedor.id > nodo.claves[i]:
                    i += 1
            # Insertar recursivamente en el hijo correcto
            self.insertar_no_lleno(nodo.hijos[i], proveedor)

    def insertar(self, proveedor):
        # Inserta un nuevo proveedor en el arbol, si la raiz estallen se divide y crea unaa nueva
        raiz = self.raiz
        if len(raiz.claves) == self.orden - 1:
            nuevo_nodo = NodoB(self.orden, hoja=False)
            nuevo_nodo.hijos.append(raiz)
            self.raiz = nuevo_nodo
            self.dividir_nodo(nuevo_nodo, 0, raiz)
            self.insertar_no_lleno(nuevo_nodo, proveedor)
        else:
            self.insertar_no_lleno(raiz, proveedor)

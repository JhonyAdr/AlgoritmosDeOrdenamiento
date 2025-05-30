import time


class AlgoritmosBusqueda:
    def __init__(self):
        self.contador_comparaciones = 0

    def establecer_contador_comparaciones(self, valor):
        self.contador_comparaciones = valor

    def obtener_contador_comparaciones(self):
        return self.contador_comparaciones

    def busqueda_lineal(self, conjunto, valor_buscar, dibujar_datos, velocidad):
        self.establecer_contador_comparaciones(0)
        for i in range(len(conjunto)):
            self.contador_comparaciones += 1
            dibujar_datos(conjunto, ['#764AF1' if x == i else '#FF597B' for x in range(len(conjunto))])
            time.sleep(velocidad)
            if conjunto[i] == valor_buscar:
                dibujar_datos(conjunto, ['#019267' if x == i else '#FF597B' for x in range(len(conjunto))])
                return i
        return -1

    def busqueda_binaria(self, conjunto, valor_buscar, dibujar_datos, velocidad):
        self.establecer_contador_comparaciones(0)
        izquierda = 0
        derecha = len(conjunto) - 1

        while izquierda <= derecha:
            self.contador_comparaciones += 1
            medio = (izquierda + derecha) // 2

            # Colorear el rango de búsqueda
            colores = ['#FF597B' for _ in range(len(conjunto))]
            for i in range(izquierda, derecha + 1):
                colores[i] = '#764AF1'
            colores[medio] = '#019267'
            dibujar_datos(conjunto, colores)
            time.sleep(velocidad)

            if conjunto[medio] == valor_buscar:
                dibujar_datos(conjunto, ['#019267' if x == medio else '#FF597B' for x in range(len(conjunto))])
                return medio
            elif conjunto[medio] < valor_buscar:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return -1

    def busqueda_texto(self, texto, patron, dibujar_datos, velocidad):
        self.establecer_contador_comparaciones(0)
        n = len(texto)
        m = len(patron)

        for i in range(n - m + 1):
            self.contador_comparaciones += 1
            j = 0
            while j < m and texto[i + j] == patron[j]:
                j += 1
                self.contador_comparaciones += 1

            # Visualizar la búsqueda
            colores = ['#FF597B' for _ in range(n)]
            for k in range(i, i + m):
                if k < n:
                    colores[k] = '#764AF1'
            dibujar_datos([ord(c) for c in texto], colores)
            time.sleep(velocidad)

            if j == m:
                # Encontrado
                colores = ['#FF597B' for _ in range(n)]
                for k in range(i, i + m):
                    colores[k] = '#019267'
                dibujar_datos([ord(c) for c in texto], colores)
                return i

        return -1